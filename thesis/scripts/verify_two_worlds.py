#!/usr/bin/env python3
"""Fresh two-fair-bit noise enumeration and pointwise public-error optimization.
No imports from other scientific scripts; no stored answers used as inputs.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse, json

BITS=list(product((0,1),repeat=2))
U=(F(1,4),)*4

def tv(a,b): return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def enumerate_model(L,Q):
    P=L*Q; counts=Counter()
    for z in range(P):
        for noise_bits in product((0,1),repeat=4):
            xs=[(z+noise_bits[2*i]-noise_bits[2*i+1])%P for i in range(2)]
            counts[z,tuple(x//Q for x in xs),tuple(x%2 for x in xs)]+=1
    den=P*16; assert sum(counts.values())==den
    marginal=defaultdict(Counter)
    for (z,y,b),c in counts.items(): marginal[y][b]+=c
    laws={y:tuple(F(c[b],sum(c.values())) for b in BITS) for y,c in marginal.items()}
    masses={y:F(sum(c.values()),den) for y,c in marginal.items()}
    return counts,den,laws,masses

def row_lp(a,b,nu,lam):
    import numpy as np
    from scipy.optimize import linprog
    # Variables K[4], |a K-a nu|[4], |b K-b U|[4].
    cost=np.r_[np.zeros(4),np.full(4,.5),np.full(4,float(lam)/2)]
    A=[];rhs=[]
    for offset,w,law in [(4,a,nu),(8,b,U)]:
        for j in range(4):
            for sign in [1,-1]:
                row=np.zeros(12);row[j]=sign*float(w);row[offset+j]=-1
                A.append(row);rhs.append(sign*float(w*law[j]))
    eq=np.r_[np.ones(4),np.zeros(8)]
    res=linprog(cost,A_ub=A,b_ub=rhs,A_eq=[eq],b_eq=[1],bounds=(0,None),method='highs')
    assert res.success,res.message
    k=res.x[:4]
    residual=max(abs(sum(k)-1),max(0,-min(k)),max(0,float(np.max(np.asarray(A)@res.x-np.asarray(rhs)))))
    measured=float(a)*sum(abs(float(nu[j])-k[j]) for j in range(4))/2+float(lam*b)*sum(abs(.25-k[j]) for j in range(4))/2
    expected=min(a,lam*b)*tv(nu,U)
    err=max(abs(res.fun-float(expected)),abs(measured-res.fun))
    assert err<1e-9 and residual<1e-9,(err,residual)
    return err,residual

def run(skip_lp):
    records=[];lp_calls=0;error=residual=0.;weighted_cases=0;total_tuples=0;ties=0
    for Q in [4,6,8,12]:
        for L in [3,4,7,10,16,20,32]:
            counts,den,laws,masses=enumerate_model(L,Q);total_tuples+=den
            b=F(1,L*L);ys=list(product(range(L),repeat=2))
            ac=F(4*Q-3,4*L*Q);am=F(3,8*L*Q)
            dc=F(1,8*Q-6);dm=F(5,12)
            assert len(laws)==3*L
            source_tv=sum((abs(masses.get(y,F(0))-b) for y in ys),F(0))/2
            assert source_tv==1-F(3,4*Q)-F(1,L)+2*L*max(F(0),am-b)
            for y in ys:
                a=masses.get(y,F(0));nu=laws.get(y,U)
                mixed=y[0]!=y[1] and ((y[1]-y[0])%L in [1,L-1])
                assert a==(ac if y[0]==y[1] else am if mixed else 0)
                assert tv(nu,U)==(dc if y[0]==y[1] else dm if mixed else 0)
            lams=sorted({F(0),F(1,2),F(1),F(2),am/b,ac/b,(am/b)/2,2*ac/b})
            for lam in lams:
                weighted_cases+=1
                val=F(0);e0=e1=F(0)
                for y in ys:
                    a=masses.get(y,F(0));nu=laws.get(y,U)
                    k=nu if a>lam*b else U
                    e1+=a*tv(nu,k);e0+=b*tv(U,k)
                    val+=min(a,lam*b)*tv(nu,U)
                    if a>0 and a==lam*b:
                        k=tuple((u+v)/2 for u,v in zip(nu,U))
                        assert a*tv(nu,k)+lam*b*tv(U,k)==min(a,lam*b)*tv(nu,U)
                        ties+=1
                formula=L*min(ac,lam*b)*dc+2*L*min(am,lam*b)*dm
                assert val==formula==e1+lam*e0
                if lam==1:
                    assert val==F(1,L*(8*Q-6))+min(F(5,16*Q),F(5,6*L))
                    records.append(dict(L=L,Q=Q,source_target_atoms=len(counts),global_sum=str(val),real_error=str(e1),null_error=str(e0),mixed_rule='posterior' if am>b else 'fair_or_tie' if am==b else 'fair'))
                if not skip_lp:
                    reps=[(0,0),(0,1),(1,0)]+([(0,2)] if L>=4 else [])
                    for y in reps:
                        er,re=row_lp(masses.get(y,F(0)),b,laws.get(y,U),lam)
                        error=max(error,er);residual=max(residual,re);lp_calls+=1
            # Independently calculate the strong and public objectives of the new sum-optimal rule.
            if (L,Q)==(4,4):
                nu=laws[(0,0)]
                assert tv(nu,U)==F(1,26)
                assert tv(nu,(F(1,9),F(2,9),F(2,9),F(4,9)))==F(41,234)
                assert tv(nu,(F(1),F(0),F(0),F(0)))==F(19,26)
                assert F(1,4)*(2*F(1,26)+2*F(9,16)*F(41,234)+2*F(1,16)*F(19,26))==F(19,208)
                kernel={y: laws.get(y,U) if masses.get(y,0)>b else U for y in ys}
                fibers=defaultdict(Counter)
                for (z,y,bit),c in counts.items():fibers[z,y][bit]+=c
                strong=sum((F(sum(c.values()),den)*tv(tuple(F(c[x],sum(c.values())) for x in BITS),kernel[y]) for (z,y),c in fibers.items()),F(0))
                measured_real=sum((masses.get(y,F(0))*tv(laws.get(y,U),kernel[y]) for y in ys),F(0))
                measured_null=sum((b*tv(U,kernel[y]) for y in ys),F(0))
                assert (strong,measured_real,measured_null,measured_real+measured_null)==(F(77,416),F(5,64),F(1,104),F(73,832))
                example={'strong':str(strong),'public_real':str(measured_real),'public_null':str(measured_null),'sum':str(measured_real+measured_null)}
                rr=records[-1];assert F(rr['global_sum'])==F(73,832) and F(rr['real_error'])==F(5,64) and F(rr['null_error'])==F(1,104)
    return dict(status='PASS',model_domains=len(records),source_distance_checks=len(records),constant_pair_example_checked=True,elementary_state_noise_bit_tuples=total_tuples,weighted_objectives_checked=weighted_cases,exact_tied_rows_checked=ties,numerical_row_lps=lp_calls,max_objective_error=error,max_constraint_residual=residual,tolerance=1e-9,lp_skipped=skip_lp,example_L4_Q4=example,cases=records)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--skip-lp',action='store_true');args=ap.parse_args()
    if args.out.exists():raise SystemExit('Choose a fresh output path.')
    result=run(args.skip_lp);args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
