#!/usr/bin/env python3
"""Optional numerical cross-check, independent LP formulation of both risks."""
import argparse, json
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);a=ap.parse_args()
    out=Path(a.out)
    if out.exists(): raise SystemExit('Choose a fresh output path.')
    results=[]
    for P in (4,8,12,16):
      for Q in range(2,P,2):
        if P%Q: continue
        L=P//Q
        for eta in (0.,.125,.1875,.25):
          M=np.zeros((P,L));t=np.zeros(P)
          for z in range(P):
            for e,p in ((-1,eta),(0,1-2*eta),(1,eta)):
              M[z,((z+e)%P)//Q]+=p
              if (z+e)%2==0:t[z]+=p
          # q_y = simulated probability of the even-parity output.
          # L1 and L-infinity errors are separate LPs.
          A=np.block([[M,-np.eye(P)],[-M,-np.eye(P)]])
          b=np.r_[t,-t];cost=np.r_[np.zeros(L),np.ones(P)/P]
          avg=linprog(cost,A_ub=A,b_ub=b,bounds=[(0,1)]*L+[(0,None)]*P,method='highs')
          Aw=np.block([[M,-np.ones((P,1))],[-M,-np.ones((P,1))]])
          worst=linprog(np.r_[np.zeros(L),1.],A_ub=Aw,b_ub=b,
                        bounds=[(0,1)]*L+[(0,None)],method='highs')
          expected=(1-4*eta)/2
          assert avg.success and worst.success
          assert abs(avg.fun-expected)<1e-9 and abs(worst.fun-expected)<1e-9
          results.append(dict(P=P,Q=Q,eta=eta,average=float(avg.fun),worst=float(worst.fun),expected=expected))
    data=dict(status='PASS_NUMERICAL_ONLY',scipy=scipy.__version__,numpy=np.__version__,
              tolerance=1e-9,linear_programs=2*len(results),results=results)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status=data['status'],linear_programs=data['linear_programs'])))
if __name__=='__main__': main()
