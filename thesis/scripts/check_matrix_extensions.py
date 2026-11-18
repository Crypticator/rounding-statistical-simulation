#!/usr/bin/env python3
"""Additional finite checks for Chapters 7–8; no delivered results imported.

Exact group images, subset-state reachability and rational capacity allocations
are separated from floating-point transport LPs. These are author checks.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
import argparse, itertools as it, math, json


def neg(r, P):
    return tuple((-v) % P for v in r)


def canonical(A, P):
    return tuple(sorted(min(r, neg(r, P)) for r in A))


def images(A, P):
    out=set()
    for order in it.permutations(range(len(A))):
        for signs in it.product((-1,1), repeat=len(A)):
            out.add(tuple(tuple(signs[i]*x % P for x in A[order[i]])
                          for i in range(len(A))))
    return out


def is_toeplitz(A):
    return all(A[i][j]==A[i-1][j-1] for i in range(1,len(A))
               for j in range(1,len(A[0])))


def is_hankel(A):
    return all(A[i][j]==A[i-1][j+1] for i in range(1,len(A))
               for j in range(len(A[0])-1))


def subset_reachable(A, P):
    choices=[tuple(dict.fromkeys((r,neg(r,P)))) for r in A]
    states={(1<<i,i,o) for i in range(len(A)) for o in range(len(choices[i]))}
    for size in range(1,len(A)):
        nxt=set()
        for used,last,orient in states:
            prev=choices[last][orient]
            for j in range(len(A)):
                if used & (1<<j):
                    continue
                for o,row in enumerate(choices[j]):
                    if row[1:]==prev[:-1]:
                        nxt.add((used|(1<<j),j,o))
        states=nxt
        if not states:
            return False
    return bool(states)


def group_checks():
    domains=[]
    for P,m,n in [(4,2,2),(4,2,3),(4,3,2),(8,2,2)]:
        target=Counter()
        hankel=Counter()
        for t in it.product(range(P),repeat=m+n-1):
            A=tuple(tuple(t[i-j+n-1] for j in range(n)) for i in range(m))
            H=tuple(reversed(A))
            assert is_toeplitz(A) and is_hankel(H)
            assert canonical(A,P)==canonical(H,P)
            target[canonical(A,P)]+=1;hankel[canonical(H,P)]+=1
        assert target==hankel
        matrix_count=0;seen=set();orbit_count=0
        for flat in it.product(range(P),repeat=m*n):
            A=tuple(tuple(flat[i*n:(i+1)*n]) for i in range(m))
            k=canonical(A,P)
            assert subset_reachable(A,P)==(k in target)
            matrix_count+=1
            if k in seen:
                continue
            seen.add(k);orbit_count+=1
            orbit=images(A,P)
            assert all(canonical(B,P)==k for B in orbit)
            counts=Counter(k)
            predicted=math.factorial(m)//math.prod(math.factorial(c) for c in counts.values())
            predicted*=2**sum(r!=neg(r,P) for r in k)
            assert len(orbit)==predicted
            assert sum(is_toeplitz(B) for B in orbit)==target[k]
            assert sum(is_hankel(B) for B in orbit)==target[k]
            assert any(is_toeplitz(B) for B in orbit)==(k in target)
        domains.append(dict(P=P,m=m,n=n,matrices=matrix_count,
                            orbits=orbit_count,target_matrices=P**(m+n-1)))
    examples=[(((0,0),(0,0),(0,0)),1),(((0,0),(0,0),(1,0)),6),
              (((0,0),(1,0),(1,0)),12),(((0,0),(0,2),(2,0)),6),
              (((0,1),(1,1),(1,2)),48)]
    for A,size in examples:
        assert len(images(A,4))==size
    A=((0,1),(1,1),(1,2))
    got={B for B in images(A,4) if is_toeplitz(B)}
    plus=((1,2),(1,1),(0,1));minus=tuple(neg(r,4) for r in plus)
    assert got=={plus,minus}
    A=((1,0),(2,3));assert not subset_reachable(A,8)
    assert tuple(tuple(sum(A[i][k]*A[k][j] for k in range(2))%8 for j in range(2)) for i in range(2))==((1,0),(0,1))
    return dict(domains=domains,matrices=sum(x['matrices'] for x in domains),
                target_matrices=sum(x['target_matrices'] for x in domains),
                direct_orbits=sum(x['orbits'] for x in domains),
                stabilizer_examples=5,explicit_two_target_orbit=True,column_boundary=True)


def allocate(p,q,alpha,strict=False):
    r=[min(alpha*y,x) for x,y in zip(p,q)]
    deficit=alpha-sum(r)
    for i in range(len(p)):
        if strict and q[i]==0:
            continue
        extra=min(deficit,p[i]-r[i]);r[i]+=extra;deficit-=extra
    assert deficit==0
    assert sum(r)==alpha and all(0<=x<=cap for x,cap in zip(r,p))
    return r


def capacity_checks(skip_lp=False):
    probs=[tuple(F(x,4) for x in (a,b,4-a-b)) for a in range(5) for b in range(5-a)]
    alphas=[F(1,4),F(1,2),F(3,4),F(1)]
    blocks=[(0,1),(2,3,4),(5,)]
    source_weights=[(F(1,3),F(2,3)),(F(1,6),F(2,6),F(3,6)),(F(1),)]
    target_weights=[tuple(reversed(x)) for x in source_weights]
    pairs=[(i,j) for block in blocks for i in block for j in block]
    if not skip_lp:
        import numpy as np
        from scipy.optimize import linprog
        E=len(pairs)
        src=np.array([i for i,j in pairs]);dst=np.array([j for i,j in pairs])
        A=np.zeros((18,E+6))
        for k,(i,j) in enumerate(pairs):
            A[i,k]=1
        A[6:12,E:]=-np.eye(6);A[12:18,E:]=-np.eye(6)
        Aeq=np.zeros((1,E+6));Aeq[0,:E]=1
        objective=np.r_[np.zeros(E),np.ones(6)/2]
    count=0;strict_feasible=0;lp_pass=0;lp_infeasible=0;max_residual=0.;max_error=0.
    for p,q in it.product(probs,repeat=2):
        mu=[F(0)]*6;nu=[F(0)]*6
        for k,block in enumerate(blocks):
            for i,w,v in zip(block,source_weights[k],target_weights[k]):
                mu[i]=p[k]*w;nu[i]=q[k]*v
        support=sum(x for x,y in zip(p,q) if y>0)
        for alpha in alphas:
            expected=sum(max(F(0),y-x/alpha) for x,y in zip(p,q))
            r=allocate(p,q,alpha)
            assert sum(abs(x/alpha-y) for x,y in zip(r,q))/2==expected
            assert expected==0 if all(alpha*y<=x for x,y in zip(p,q)) else expected>0
            count+=1
            if alpha<=support:
                rr=allocate(p,q,alpha,True)
                assert all(q[i]>0 or rr[i]==0 for i in range(3))
                assert sum(abs(x/alpha-y) for x,y in zip(rr,q))/2==expected
                strict_feasible+=1
            if skip_lp:
                continue
            af=float(alpha);Ap=A.copy()
            for k,(i,j) in enumerate(pairs):
                Ap[6+j,k]=1/af;Ap[12+j,k]=-1/af
            rhs=np.r_[np.array(mu,float),np.array(nu,float),-np.array(nu,float)]
            for strict in [False,True]:
                bounds=[(0,0 if strict and nu[j]==0 else None) for i,j in pairs]+[(0,None)]*6
                result=linprog(objective,A_ub=Ap,b_ub=rhs,A_eq=Aeq,b_eq=[af],bounds=bounds,method='highs')
                if strict and alpha>support:
                    assert result.status==2,result.message;lp_infeasible+=1;continue
                assert result.success,result.message
                err=abs(result.fun-float(expected));assert err<1e-8
                residual=max(float(np.max(Ap@result.x-rhs)),abs(float(sum(result.x[:E]))-af),0.)
                assert residual<1e-8
                mass=np.bincount(dst,weights=result.x[:E],minlength=6)/af
                assert abs(sum(abs(mass-np.array(nu,float)))/2-result.fun)<1e-8
                max_error=max(max_error,err);max_residual=max(max_residual,residual);lp_pass+=1
    return dict(probability_vectors=len(probs),partition_block_sizes=[2,3,1],
                alphas=list(map(str,alphas)),exact_allocations=count,
                exact_support_restricted_allocations=strict_feasible,
                transport_lp_feasible=lp_pass,transport_lp_infeasible=lp_infeasible,
                transport_lp_total=lp_pass+lp_infeasible,
                maximum_objective_error=max_error,maximum_constraint_residual=max_residual,
                lp_tolerance=1e-8,lp_skipped=skip_lp)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--skip-lp',action='store_true');args=ap.parse_args()
    p=Path(args.out)
    if p.exists():raise SystemExit('Output already exists')
    out=dict(status='PASS',group=group_checks(),capacity=capacity_checks(args.skip_lp))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
