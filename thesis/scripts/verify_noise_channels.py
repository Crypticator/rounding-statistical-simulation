#!/usr/bin/env python3
"""Exact finite checks for Chapters 5 and 6. Standard library only; stored results are never read."""
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

