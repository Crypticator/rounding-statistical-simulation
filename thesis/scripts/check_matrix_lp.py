#!/usr/bin/env python3
"""Independent matrix-level transport LP; no canonical-orbit routine imported.
Float64 corroboration only. It neither reads prior results nor certifies proofs.
"""
import argparse
import itertools as it
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def problem(p,m,n):
    matrices=list(it.product(range(p),repeat=m*n)); N=len(matrices)
    index={a:i for i,a in enumerate(matrices)}
    source=[]; dest=[]
    perms=list(it.permutations(range(m)))
    signs=list(it.product((-1,1),repeat=m))
    for i,a in enumerate(matrices):
        reachable=set()
        for perm in perms:
            for sg in signs:
                b=tuple((sg[r]*a[perm[r]*n+c])%p for r in range(m) for c in range(n))
                reachable.add(index[b])
        for j in sorted(reachable):source.append(i);dest.append(j)
    E=len(source)
    q=np.array([float(all(a[r*n+c]==a[(r-1)*n+c-1]
                         for r in range(1,m) for c in range(1,n)))/p**(m+n-1)
                for a in matrices])
    return N,E,np.array(source),np.array(dest),q


def solve(p,m,n,alphas):
    N,E,src,dst,q=problem(p,m,n);out=[]
    eidx=np.arange(E);vidx=E+np.arange(N)
    for af in alphas:
        a=float(af)
        rr=np.concatenate([src,N+dst,2*N+dst,N+np.arange(N),2*N+np.arange(N)])
        cc=np.concatenate([eidx,eidx,eidx,vidx,vidx])
        vv=np.concatenate([np.ones(E),np.ones(E)/a,-np.ones(E)/a,-np.ones(N),-np.ones(N)])
        Aub=coo_matrix((vv,(rr,cc)),shape=(3*N,E+N)).tocsr()
        bub=np.concatenate([np.ones(N)/N,q,-q])
        Aeq=coo_matrix((np.ones(E),(np.zeros(E,dtype=int),eidx)),shape=(1,E+N)).tocsr()
        c=np.concatenate([np.zeros(E),np.ones(N)/2])
        r=linprog(c,A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=[a],bounds=(0,None),method='highs')
        assert r.success,r.message
        residual=max(float(np.max(Aub@r.x-bub)),abs(float(np.sum(r.x[:E]))-a),0)
        assert residual<1e-8
        # Exact expected values are separately derived in the manuscript.
        expected={(4,2,2,F(1,4)):F(0),(4,2,2,F(1,2)):F(3,32),
                  (4,2,2,F(1)):F(25,64),
                  (4,3,2,F(1,16)):F(0),(4,3,2,F(1,2)):F(139,512),
                  (4,3,2,F(1)):F(539,1024)}
        target=expected.get((p,m,n,af))
        if target is not None:assert abs(r.fun-float(target))<1e-8,(p,m,n,af,r.fun,target)
        out.append({'P':p,'m':m,'n':n,'matrices':N,'flow_variables':E,
                    'acceptance':str(af),'optimal_tv_numerical':float(r.fun),
                    'max_feasibility_residual':residual,'expected_exact':str(target) if target is not None else None})
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args();path=Path(args.out)
    if path.exists():raise SystemExit('Refusing an existing output file')
    out=solve(4,2,2,[F(1,4),F(1,2),F(1)])+solve(4,3,2,[F(1,16),F(1,2),F(1)])
    result={'status':'PASS_NUMERICAL_ONLY','numpy':np.__version__,'scipy':scipy.__version__,
            'tolerance':1e-8,'cases':out}
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
