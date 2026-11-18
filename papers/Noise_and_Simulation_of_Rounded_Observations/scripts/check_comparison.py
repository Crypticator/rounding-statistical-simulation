#!/usr/bin/env python3
"""Exact certificates comparing raw-observation and quotient-only simulation.

No theorem classification is imported. All arithmetic uses Fraction. Published
Fourier conditions are checked through explicit convolutions; no floating DFT.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json


def rank(a):
    a = [list(map(F, row)) for row in a]
    row = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(row, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        divisor = a[row][col]
        a[row] = [x / divisor for x in a[row]]
        for j in range(len(a)):
            if j != row and a[j][col]:
                multiple = a[j][col]
                a[j] = [x - multiple * y for x, y in zip(a[j], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def convolution(a, b):
    p = len(a)
    return [sum(a[e] * b[(j-e) % p] for e in range(p)) for j in range(p)]


def channels(p, q, c, b, eta):
    L = p // q
    noise = [F(0)] * p
    noise[0], noise[1], noise[-1] = 1-2*eta, eta, eta
    C = [[noise[(x-z) % p] for x in range(p)] for z in range(p)]
    M = [[sum((C[z][x] for x in range(p) if x//q == y), F(0))
          for y in range(L)] for z in range(p)]
    N = [[sum((C[z][x] for x in range(p) if ((c*x+b) % p)//q == w), F(0))
          for w in range(L)] for z in range(p)]
    return noise, C, M, N


def target_embedding(N):
    p, L = len(N), len(N[0])
    phi = [[N[z][(z+d) % p] if (z+d) % p < L else F(0)
            for d in range(p)] for z in range(p)]
    assert all(sum(row) == 1 for row in phi)
    rho = [sum(phi[z][(w-z) % p] for z in range(p))/p for w in range(p)]
    chi = {w: [phi[(w-j) % p][j]/(p*rho[w]) for j in range(p)]
           for w in range(p) if rho[w]}
    assert sum(rho) == 1
    assert all(sum(row) == 1 and min(row) >= 0 for row in chi.values())
    return rho, chi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    if args.out.exists():
        raise SystemExit('Refusing to overwrite an existing output')
    noise, C, M, N = channels(8, 2, 2, 0, F(1, 8))
    rho, chi = target_embedding(N)
    tau = [F(1, 2) if j in (0, 4) else F(0) for j in range(8)]
    assert rho == [F(1, 4)]*4 + [F(0)]*4
    assert all(convolution(noise, tau) == v for v in chi.values())
    rC, rM = rank(C), rank(M)
    rAug = rank([row + [N[z][0]] for z, row in enumerate(M)])
    assert (rC, rM, rAug) == (8, 4, 5)
    # Invertible C implies full Fourier support. Explicit nonnegative tau
    # therefore is the unique normalized inverse in Theorem 2's condition.
    first = {'P':8, 'Q':2, 'c':2, 'b':0, 'eta':'1/8',
             'rho':list(map(str,rho)), 'tau':list(map(str,tau)),
             'rank_C':rC,'rank_M':rM,'rank_augmented_column_0':rAug,
             'raw_LWE_OD_sufficient_conditions':'PASS',
             'quotient_only_linear_feasibility':False}
    noise, C, M, N = channels(8, 2, 4, 0, F(1, 4))
    rho, chi = target_embedding(N)
    uniform = [F(1,8)]*8
    assert set(chi) == {0,2}
    assert all(v == uniform for v in chi.values())
    assert convolution(noise, uniform) == uniform
    assert all(sum(C[z][x] * (-1)**x for x in range(8)) == 0 for z in range(8))
    assert rank(C) == 7
    coin = [F(1,2),F(0),F(1,2),F(0)]
    assert N == [coin]*8
    # K(y,.)=coin. Since rows of M sum to 1, MK=N.
    assert all(sum(row)==1 for row in M)
    tv = F(0)
    for z in range(8):
        for y in range(4):
            for w in range(4):
                real = sum((C[z][x] for x in range(8)
                           if x//2 == y and ((4*x)%8)//2 == w), F(0))/8
                simulated = M[z][y]*coin[w]/8
                tv += abs(real-simulated)/2
    assert tv == F(1,4)
    second = {'P':8,'Q':2,'c':4,'b':0,'eta':'1/4',
              'rank_C':7,'spectral_zero':'k=P/2=4',
              'active_chi':'uniform on Z_8','canonical_tau':'uniform on Z_8',
              'raw_LWE_OD_sufficient_conditions':'PASS',
              'quotient_kernel':list(map(str,coin)),
              'TV_ZW':'0','TV_ZYW':str(tv)}
    result = {'status':'PASS','arithmetic':'fractions.Fraction',
              'scope':'Two exact comparison certificates; no novelty certification',
              'cases':[first,second]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
