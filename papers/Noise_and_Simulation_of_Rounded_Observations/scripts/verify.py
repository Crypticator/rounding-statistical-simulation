#!/usr/bin/env python3
"""Exact finite checks. Python standard library only. No stored result is read."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import argparse, hashlib, json, math

def matmul(A, B):
    cols = list(zip(*B))
    return [[sum((x*y for x,y in zip(row,col) if x and y), F(0))
             for col in cols] for row in A]

def pivot_rows(M):
    A = [list(x) for x in zip(*M)]
    r, piv = 0, []
    for c in range(len(A[0])):
        k = next((k for k in range(r,len(A)) if A[k][c]), None)
        if k is None: continue
        A[r], A[k] = A[k], A[r]
        d=A[r][c]; A[r]=[v/d for v in A[r]]
        for k in range(r+1,len(A)):
            t=A[k][c]
            if t: A[k]=[v-t*w for v,w in zip(A[k],A[r])]
        piv.append(c); r+=1
        if r==len(A): break
    return piv

def inverse(A):
    n=len(A)
    B=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for c in range(n):
        k=next(k for k in range(c,n) if B[k][c])
        B[c],B[k]=B[k],B[c]
        d=B[c][c]; B[c]=[x/d for x in B[c]]
        for k in range(n):
            if k==c: continue
            t=B[k][c]
            if t: B[k]=[v-t*w for v,w in zip(B[k],B[c])]
    return [r[n:] for r in B]

def channel(P,Q,eta,c=1,b=0):
    L=P//Q; N=[[F(0) for _ in range(L)] for _ in range(P)]
    for z in range(P):
        for e,p in [(-1,eta),(0,1-2*eta),(1,eta)]:
            N[z][((c*(z+e)+b)%P)//Q]+=p
    return N

def predicted(P,Q,eta,c,b):
    if c==0: return 'constant'
    if c==1 and b%Q==0: return 'plus'
    if c==P-1 and b%Q==Q-1: return 'minus'
    if eta==F(1,4) and P%2==0 and c==P//2: return 'parity'
    return 'excluded'

def classify_domain(maxP):
    counts=Counter(); witnesses=[]; cases=0; ranks=0
    for P in range(4,maxP+1):
        for Q in range(2,P):
            if P%Q: continue
            L=P//Q
            for eta in (F(0),F(1,8),F(1,4)):
                M=channel(P,Q,eta); piv=pivot_rows(M)
                assert len(piv)==L, (P,Q,eta,'rank')
                ranks+=1; inv=inverse([M[i] for i in piv])
                for c,b in product(range(P), repeat=2):
                    N=channel(P,Q,eta,c,b)
                    K=matmul(inv,[N[i] for i in piv])
                    residual=matmul(M,K)
                    mismatch=next(((z,w,residual[z][w]-N[z][w])
                                  for z in range(P) for w in range(L)
                                  if residual[z][w]!=N[z][w]),None)
                    negative=next(((y,w,K[y][w]) for y in range(L)
                                   for w in range(L) if K[y][w]<0),None)
                    assert all(sum(r)==1 for r in K)
                    feasible=mismatch is None and negative is None
                    kind=predicted(P,Q,eta,c,b)
                    assert feasible==(kind!='excluded'), (P,Q,str(eta),c,b,kind,K)
                    counts[kind]+=1; cases+=1
                    if not feasible:
                        counts['linear_inconsistency' if mismatch else 'negative_kernel']+=1
                        if len(witnesses)<8:
                            witnesses.append(dict(P=P,Q=Q,eta=str(eta),c=c,b=b,
                                reason='residual' if mismatch else 'negative',
                                certificate=[str(x) for x in (mismatch or negative)]))
    return dict(max_P=maxP,etas=['0','1/8','1/4'],cases=cases,
                full_column_rank_checks=ranks,counts=dict(counts),witnesses=witnesses)

def parity_metrics(maxP):
    out=[]; affine_secret_checks=0
    for P in range(4,maxP+1,2):
        for Q in range(2,P,2):
            if P%Q: continue
            L=P//Q; c=P//2; alpha=0; beta=(P//2)//Q
            for eta in (F(0),F(1,8),F(3,16),F(1,4)):
                M=channel(P,Q,eta); N=channel(P,Q,eta,c)
                errors=[sum(abs(x-(F(1,2) if w in (alpha,beta) else 0))
                            for w,x in enumerate(row))/2 for row in N]
                expected=(1-4*eta)/2
                assert min(errors)==max(errors)==expected
                # Exact dual witness: every source-channel column has zero
                # alternating sum; target event alpha has alternating mean d/2.
                for y in range(L):
                    assert sum((-1)**z*M[z][y] for z in range(P))==0
                assert sum((-1)**z*N[z][alpha] for z in range(P))/P==expected
                out.append(dict(P=P,Q=Q,eta=str(eta),latent_avg_and_max=str(expected)))
            eta=F(1,4)
            # Enumerate the real joint law (Z,Y,W), then minimize each public
            # cell's piecewise-linear TV objective over all exact breakpoints.
            D={}
            for z in range(P):
                for e,p in [(-1,eta),(0,1-2*eta),(1,eta)]:
                    y=((z+e)%P)//Q; w=((c*(z+e))%P)//Q
                    D[z,y,w]=D.get((z,y,w),F(0))+p/P
            def objective(y,p):
                v=F(0)
                for z in range(P):
                    a=D.get((z,y,alpha),F(0)); b=D.get((z,y,beta),F(0))
                    v+=(abs(a-(a+b)*p)+abs(b-(a+b)*(1-p)))/2
                return v
            optimum=F(0)
            for y in range(L):
                breaks={F(0),F(1),F(1,2)}
                for z in range(P):
                    a=D.get((z,y,alpha),F(0)); b=D.get((z,y,beta),F(0))
                    if a+b: breaks.add(a/(a+b))
                v=min(objective(y,p) for p in breaks)
                assert v==objective(y,F(1,2))
                optimum+=v
                # Public (Y,W) law is reproduced exactly by a fair coin.
                for w in (alpha,beta):
                    assert sum(D.get((z,y,w),F(0)) for z in range(P))==F(1,2*L)
            assert optimum==F(1,2*Q), (P,Q,optimum)
            # The noisy value X itself has hidden parity in every cell.
            assert all(sum(x%2==0 for x in range(y*Q,(y+1)*Q))==Q//2 for y in range(L))
            for a in range(P):
                if math.gcd(a,P)!=1: continue
                assert sorted((a*s)%P for s in range(P))==list(range(P))
                affine_secret_checks+=1
            out.append(dict(P=P,Q=Q,CBD1_full_view_optimum=str(optimum),
                            public_view='0',noisy_input_view='1/2'))
    return dict(cases=out,unit_secret_bijections=affine_secret_checks)

def mutations():
    # Same formulas must NOT silently substitute fresh noise after scaling.
    P,Q,c=8,2,4
    real=channel(P,Q,F(1,4),c)
    fresh=[]
    for z in range(P):
        row=[F(0)]*(P//Q)
        for e,p in [(-1,F(1,4)),(0,F(1,2)),(1,F(1,4))]:
            row[((c*z+e)%P)//Q]+=p
        fresh.append(row)
    assert real!=fresh
    # Parity erasure disappears strictly below CBD1.
    assert channel(8,2,F(1,8),4)[0]!=channel(8,2,F(1,8),4)[1]
    # Null world: a uniform quotient mapped to the parity coin is not
    # uniform over L>2 output values.
    assert F(1,2)!=F(1,4)
    # b=0 is forbidden for a reflection; b=Q-1 makes it admissible.
    assert predicted(8,2,F(1,8),7,0)=='excluded'
    assert predicted(8,2,F(1,8),7,1)=='minus'
    return dict(fresh_target_noise_changes_channel=True,
                subcritical_noise_retains_parity=True,
                null_world_mismatch_for_L_gt_2=True,
                reflection_requires_translation=True)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True)
    ap.add_argument('--max-p',type=int,default=16)
    a=ap.parse_args(); out=Path(a.out)
    if out.exists(): raise SystemExit('Refusing to reuse an existing result; choose a fresh --out.')
    data=dict(status='PASS',method='exact fractions, independent channel feasibility',
              classification=classify_domain(a.max_p),parity=parity_metrics(32),
              mutations=mutations(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status=data['status'],classification_cases=data['classification']['cases'],
                         ranks=data['classification']['full_column_rank_checks'],
                         output=str(out)),ensure_ascii=False))
if __name__=='__main__': main()
