#!/usr/bin/env python3
"""Numerical corroboration from generic channel-table linear programs."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json
import numpy as np
from scipy.optimize import linprog
from verify_noise_channels import channel

def optimize(M,N,prior,worst=False):
    M=np.array(M,dtype=float);N=np.array(N,dtype=float)
    s,o=M.shape;r=N.shape[1];nk=o*r;nu=s*r;nv=nk+nu+int(worst)
    obj=np.zeros(nv)
    if worst:obj[-1]=1
    else:obj[nk:nk+nu]=np.repeat(np.array(prior,dtype=float)/2,r)
    eq=np.zeros((o,nv))
    for y in range(o):eq[y,y*r:(y+1)*r]=1
    aub=[];bub=[]
    for z in range(s):
        for w in range(r):
            row=np.zeros(nv)
            for y in range(o):row[y*r+w]=M[z,y]
            row[nk+z*r+w]=-1
            aub.append(row.copy());bub.append(N[z,w])
            row[:nk]*=-1
            aub.append(row.copy());bub.append(-N[z,w])
        if worst:
            row=np.zeros(nv);row[nk+z*r:nk+(z+1)*r]=.5;row[-1]=-1
            aub.append(row);bub.append(0)
    res=linprog(obj,A_ub=np.array(aub),b_ub=np.array(bub),A_eq=eq,b_eq=np.ones(o),bounds=(0,None),method='highs')
    assert res.success,res.message
    K=res.x[:nk].reshape(o,r)
    errors=np.abs(M@K-N).sum(axis=1)/2
    val=errors.max() if worst else np.dot(np.array(prior,dtype=float),errors)
    assert np.max(np.abs(K.sum(axis=1)-1))<1e-9 and K.min()>-1e-9
    assert abs(val-res.fun)<1e-9
    return float(val)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args();p=Path(args.out)
    if p.exists():raise SystemExit('Choose a fresh output path.')
    out=[]
    for P,Q in [(4,2),(6,2),(8,2),(8,4),(12,4),(12,6)]:
        for eta in [F(0),F(1,8),F(1,4)]:
            M=channel(P,Q,eta)
            for b in range(P):
                N=channel(P,Q,eta,P//2,b)
                for worst in (False,True):
                    value=optimize(M,N,[F(1,P)]*P,worst)
                    expected=float((1-4*eta)/2)
                    assert abs(value-expected)<1e-9,(P,Q,eta,b,worst,value)
                    out.append(dict(P=P,Q=Q,eta=str(eta),b=b,objective='worst' if worst else 'uniform_average',value=value,expected=expected))
    M=channel(6,3,F(0));N=channel(6,3,F(0),3)
    odd=[optimize(M,N,[F(1,6)]*6,w) for w in (False,True)]
    assert abs(odd[0]-1/3)<1e-9 and abs(odd[1]-.5)<1e-9
    M=channel(8,2,F(1,8));N=channel(8,2,F(1,8),4)
    point=optimize(M,N,[1]+[0]*7)
    assert abs(point)<1e-9
    result=dict(status='PASS',method='SciPy HiGHS floating point',tolerance=1e-9,main_programs=len(out),additional_programs=3,results=out,odd_cell_optima=odd,point_prior_optimum=point)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='results'}))

if __name__=='__main__':main()
