#!/usr/bin/env python3
"""Exact arithmetic checks. No stored results are used as input."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent

def tv(a, b):
    return sum((abs(a.get(x, 0)-b.get(x, 0)) for x in a.keys() | b.keys()), F(0))/2

def exact_joint(P, Q, k):
    """Integer weights: E=-1,0,1 have weights 1,2,1 out of 4."""
    joint = Counter()
    for z in range(P):
        for es in product((-1, 0, 1), repeat=k):
            xs = tuple((z+e) % P for e in es)
            joint[z, tuple(x//Q for x in xs), tuple(x % 2 for x in xs)] += 2**es.count(0)
    den = P*4**k
    assert sum(joint.values()) == den
    return joint, den

def directed_pair(y, L):
    cells = set(y)
    if len(cells) != 2:
        return None
    pairs = [(u, (u+1) % L) for u in cells if (u+1) % L in cells]
    return pairs[0] if len(pairs) == 1 else None

def fair(k):
    return {b: F(1, 2**k) for b in product((0, 1), repeat=k)}

def boundary_law(y, u, v, left):
    law = {}
    for b in product((0, 1), repeat=len(y)):
        pr = F(1)
        for yi, bi in zip(y, b):
            p1 = F(2, 3) if left and yi == u else (F(0) if left else (F(1) if yi == u else F(1, 3)))
            pr *= p1 if bi else 1-p1
        if pr:
            law[b] = pr
    assert sum(law.values()) == 1
    return law

def optimal(y, L):
    """Theorem's total block kernel; not claimed optimal outside Q>=4,L>=3."""
    pair = directed_pair(y, L)
    if pair is None:
        return fair(len(y))
    u, v = pair
    if y.count(u) == y.count(v):
        a, b = boundary_law(y, u, v, True), boundary_law(y, u, v, False)
        return {x: (a.get(x, 0)+b.get(x, 0))/2 for x in a.keys() | b.keys()}
    return boundary_law(y, u, v, y.count(u) > y.count(v))

def s_formula(k):
    return sum((comb(k, j)*abs(F(2**j, 3**k)-F(1, 2**k)) for j in range(k+1)), F(0))/2

def optimum_formula(Q, k):
    const = (2*F(3, 4)**k*s_formula(k)+2*F(1, 4)**k*(1-F(1, 2**k)))/Q
    mixed = sum((comb(k, ell)*3**min(ell, k-ell)*(1-F(2, 3)**max(ell, k-ell))
                 for ell in range(1, k)), F(0))/(Q*4**k)
    return const+mixed

def fair_formula(Q, k):
    overlap = F(0)
    for a in range(k+1):
        for b in range(k-a+1):
            c = k-a-b
            mult = factorial(k)//(factorial(a)*factorial(b)*factorial(c))
            overlap += mult*min(F(2**a, 4**k), F(3**(a+b), 8**k))
    return F(2, Q)*(1-overlap)

def exact_metrics(P, Q, k):
    joint, den = exact_joint(P, Q, k)
    zy, yb, yz_mass, zb = Counter(), Counter(), Counter(), Counter()
    for (z, y, b), n in joint.items():
        zy[z, y] += n
        yb[y, b] += n
        yz_mass[y] += n
        zb[z, b] += n
    assert all(zb[z, b] == den//(P*2**k) for z in range(P) for b in product((0, 1), repeat=k))
    kernels = {}
    public = {y: {b: F(yb[y, b], n) for b in product((0, 1), repeat=k)} for y, n in yz_mass.items()}
    kernels['fair'] = {y: fair(k) for y in yz_mass}
    kernels['optimal'] = {y: optimal(y, P//Q) for y in yz_mass}
    kernels['posterior'] = public
    result = dict(P=P, Q=Q, k=k, noise_tuples=P*3**k, nonzero_joint_atoms=len(joint))
    for name, kernel in kernels.items():
        err = sum((abs(F(joint[z, y, b])-n*kernel[y].get(b, 0))
                   for (z, y), n in zy.items() for b in product((0, 1), repeat=k)), F(0))/(2*den)
        err_pub = sum((abs(F(yb[y, b])-n*kernel[y].get(b, 0))
                       for y, n in yz_mass.items() for b in product((0, 1), repeat=k)), F(0))/(2*den)
        result[name+'_strong'] = str(err)
        result[name+'_public'] = str(err_pub)
    assert F(result['posterior_public']) == 0
    assert F(result['optimal_strong']) == optimum_formula(Q, k)
    assert F(result['fair_strong']) == fair_formula(Q, k)
    assert optimum_formula(Q, k) <= F(result['posterior_strong']) <= 2*optimum_formula(Q, k)
    if k == 2:
        L = P//Q
        for name in kernels:
            null = sum((tv(kernels[name].get(y, fair(k)), fair(k))
                        for y in product(range(L), repeat=k)), F(0))/L**k
            result[name+'_null'] = str(null)
        assert F(result['fair_public']) == F(7, 16*Q)
        assert F(result['optimal_public']) == F(1, 8*Q)
        assert F(result['fair_null']) == 0
        assert F(result['optimal_null']) == F(5, 6*L)
        assert F(result['posterior_null']) == F(5, 6*L)+F(1, L*(8*Q-6))
    return result

def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument("--out",type=Path,required=True); args=ap.parse_args()
    if args.out.exists(): raise SystemExit("Choose a fresh output path.")
    args.out.parent.mkdir(parents=True,exist_ok=True)
    cases = [exact_metrics(P, Q, k) for P, Q in ((12, 4), (16, 4), (18, 6), (24, 8)) for k in range(1, 7)]
    curves = [dict(k=k, optimum=str(optimum_formula(4, k)), fair=str(fair_formula(4, k))) for k in range(1, 65)]
    result = dict(status='PASS', arithmetic='fractions.Fraction and integers', cases=cases,
                  enumeration_cases=len(cases), noise_tuples=sum(x['noise_tuples'] for x in cases),
                  total_nonzero_joint_atoms=sum(x['nonzero_joint_atoms'] for x in cases), curves_Q4=curves)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('cases', 'curves_Q4')}))
    print(json.dumps([x for x in cases if x['P'] == 16 and x['k'] <= 3], indent=2))

if __name__ == '__main__':
    main()
