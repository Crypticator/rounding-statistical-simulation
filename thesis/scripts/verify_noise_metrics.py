#!/usr/bin/env python3
"""Exact channel and joint-law checks for Chapters 5 and 6; no stored oracles."""
from fractions import Fraction as F
from pathlib import Path
import argparse, json
from verify_noise_channels import channel, pivot_rows

def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def parity_checks(max_p=24):
    records=[]; joint_records=[]; odd_records=[]
    for P in range(4,max_p+1,2):
        for Q in range(2,P):
            if P%Q: continue
            L=P//Q; c=P//2
            if Q%2:
                for b in range(P):
                    G=channel(P,Q,F(0),c,b)
                    costs=[]
                    for y in range(L):
                        masses=[sum(G[x][w] for x in range(Q*y,Q*(y+1))) for w in range(L)]
                        costs.append(1-max(masses)/Q)
                        # Both targets occur, so any row has worst loss >= 1/2.
                        assert sum(v>0 for v in masses)==2
                    avg=sum(costs,F(0))/L
                    assert avg==F(Q-1,2*Q)
                    odd_records.append(dict(P=P,Q=Q,b=b,average=str(avg),worst='1/2'))
                continue
            for eta in (F(0),F(1,16),F(1,8),F(3,16),F(1,4)):
                M=channel(P,Q,eta)
                assert all(sum((-1)**z*M[z][y] for z in range(P))==0 for y in range(L))
                for b in range(P):
                    alpha=b//Q; beta=((b+P//2)%P)//Q
                    assert alpha!=beta
                    rho=[F(1,2) if w in (alpha,beta) else F(0) for w in range(L)]
                    N=channel(P,Q,eta,c,b)
                    expected=(1-4*eta)/2
                    errs=[tv(r,rho) for r in N]
                    witness=sum((-1)**z*N[z][alpha] for z in range(P))/P
                    assert min(errs)==max(errs)==witness==expected
                    records.append(dict(P=P,Q=Q,b=b,eta=str(eta),lower_bound=str(witness),attained_error=str(errs[0])))
            for b in range(P):
                alpha=b//Q; beta=((b+P//2)%P)//Q
                D={}
                for z in range(P):
                    for e,p in [(-1,F(1,4)),(0,F(1,2)),(1,F(1,4))]:
                        x=(z+e)%P;y=x//Q;w=((c*x+b)%P)//Q
                        D[z,y,w]=D.get((z,y,w),F(0))+p/P
                optimum=F(0); boundaries=[]
                for y in range(L):
                    pairs=[(D.get((z,y,alpha),F(0)),D.get((z,y,beta),F(0))) for z in range(P)]
                    breaks={F(0),F(1),F(1,2)}|{a/(a+d) for a,d in pairs if a+d}
                    def objective(p):
                        return sum((abs(a-(a+d)*p)+abs(d-(a+d)*(1-p)) for a,d in pairs),F(0))/2
                    val=min(objective(p) for p in breaks)
                    assert val==objective(F(1,2))
                    optimum+=val
                    assert sum(a for a,d in pairs)==sum(d for a,d in pairs)==F(1,2*L)
                for z in range(P):
                    err=F(0)
                    for y in range(L):
                        a=D.get((z,y,alpha),F(0))*P;d=D.get((z,y,beta),F(0))*P
                        err+=(abs(a-(a+d)/2)+abs(d-(a+d)/2))/2
                    assert err==(F(1,4) if z%Q in (0,Q-1) else 0)
                    boundaries.append(str(err))
                assert optimum==F(1,2*Q)
                rho=[F(1,2) if w in (alpha,beta) else F(0) for w in range(L)]
                null=tv(rho,[F(1,L)]*L)
                assert null==1-F(2,L)
                joint_records.append(dict(P=P,Q=Q,b=b,joint_optimum=str(optimum),public_error='0',raw_input_optimum='1/2',null_error=str(null)))
    return dict(domain_max_P=max_p,all_translations=True,etas=['0','1/16','1/8','3/16','1/4'],
                statewise_cases=len(records),statewise=records,joint_cases=len(joint_records),joint=joint_records,
                noiseless_odd_cell_cases=len(odd_records),noiseless_odd_cell=odd_records)

def uniform_noise_checks():
    cases=0
    for P in (4,6,8,9,10,12):
        for Q in range(2,P):
            if P%Q:continue
            L=P//Q
            for c in range(P):
                for b in range(P):
                    K=[[F(0)]*L for _ in range(L)]
                    for x in range(P):K[x//Q][((c*x+b)%P)//Q]+=F(1,Q)
                    for z in range(P):
                        J=[[F(0)]*L for _ in range(L)]
                        for e in range(P):
                            x=(z+e)%P;J[x//Q][((c*x+b)%P)//Q]+=F(1,P)
                        assert all(J[y][w]==K[y][w]/L for y in range(L) for w in range(L))
                    cases+=1
    return dict(moduli=[4,6,8,9,10,12],all_proper_divisors=True,all_c_and_b=True,cases=cases,all_state_joint_equalities=True)

def concrete_checks():
    M=channel(8,2,F(1,8));N=channel(8,2,F(1,8),2)
    ranks=[len(pivot_rows(M)),len(pivot_rows([r+[n[0]] for r,n in zip(M,N)]))]
    assert ranks==[4,5]
    real=channel(8,2,F(1,4),4)[0]
    fresh=[F(0)]*4
    for e,p in [(-1,F(1,4)),(0,F(1,2)),(1,F(1,4))]:fresh[(e%8)//2]+=p
    assert real==[F(1,2),0,F(1,2),0] and fresh==[F(3,4),0,0,F(1,4)]
    actual={(3,2):F(1,4),(0,0):F(1,2),(0,2):F(1,4)}
    sim={(3,0):F(1,8),(3,2):F(1,8),(0,0):F(3,8),(0,2):F(3,8)}
    distance=sum((abs(actual.get(k,0)-sim.get(k,0)) for k in actual.keys()|sim.keys()),F(0))/2
    assert distance==F(1,4)
    return dict(raw_access_rank_certificate=ranks,fresh_noise_real=[str(x) for x in real],
                fresh_noise_wrong_model=[str(x) for x in fresh],worked_joint_distance=str(distance))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
    p=Path(args.out)
    if p.exists():raise SystemExit('Choose a fresh output path.')
    result=dict(status='PASS',arithmetic='fractions.Fraction',parity=parity_checks(),uniform_noise=uniform_noise_checks(),examples=concrete_checks())
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',statewise_cases=result['parity']['statewise_cases'],joint_cases=result['parity']['joint_cases'],odd_cell_cases=result['parity']['noiseless_odd_cell_cases'],uniform_noise_cases=result['uniform_noise']['cases'])))

if __name__=='__main__':main()
