#!/usr/bin/env python3
"""Independent enumeration by two fair bits per CBD1 noise; TV LP.
Does not import verify or read its results/formula.
LP arithmetic is floating point, so this is a check, not an exact proof.
"""
from itertools import product
from collections import Counter, defaultdict
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parent.parent

def solve(P, Q, k):
    grouped = defaultdict(Counter)
    for z in range(P):
        for bits in product((0, 1), repeat=2*k):
            xs = [(z+bits[2*i]-bits[2*i+1]) % P for i in range(k)]
            grouped[tuple(x//Q for x in xs)][z, tuple(x & 1 for x in xs)] += 1
    bs = list(product((0, 1), repeat=k))
    total = P*4**k
    objective = 0.0
    residual = 0.0
    public_min = null_min = 0.0
    solves = 0
    for y, counts in grouped.items():
        zs = sorted({z for z, b in counts})
        n = sum(counts.values())
        mass = {z: sum(counts[z, b] for b in bs)/n for z in zs}
        d = len(bs)
        nvar = d+len(zs)*d
        cost = np.r_[np.zeros(d), np.full(len(zs)*d, 0.5)]
        rows, rhs = [], []
        for zi, z in enumerate(zs):
            for bi, b in enumerate(bs):
                s = d+zi*d+bi
                row = np.zeros(nvar); row[bi] = mass[z]; row[s] = -1
                rows.append(row); rhs.append(counts[z, b]/n)
                row = np.zeros(nvar); row[bi] = -mass[z]; row[s] = -1
                rows.append(row); rhs.append(-counts[z, b]/n)
        A = np.asarray(rows); rhs = np.asarray(rhs)
        eq = np.r_[np.ones(d), np.zeros(nvar-d)][None, :]
        ans = linprog(cost, A_ub=A, b_ub=rhs, A_eq=eq, b_eq=[1.0], bounds=(0, None), method='highs')
        assert ans.success, ans.message
        solves += 1
        residual = max(residual, float(np.max(A@ans.x-rhs)), abs(sum(ans.x[:d])-1), max(0, -float(np.min(ans.x))))
        objective += n/total*ans.fun
        if k == 2 and Q >= 4 and P//Q >= 3:
            # Lexicographic LP: retain the minimum strong-view error,
            # then minimize separately public-real / public-null error.
            # 1e-12 feasibility allowance is explicitly recorded.
            targets = [np.array([sum(counts[z, b] for z in zs)/n for b in bs]), np.full(d, 1/d)]
            vals = []
            for target in targets:
                A2 = [np.r_[row, np.zeros(d)] for row in A]
                rhs2 = list(rhs)
                A2.append(np.r_[cost, np.zeros(d)]); rhs2.append(ans.fun+1e-12)
                for bi in range(d):
                    row = np.zeros(nvar+d); row[bi] = 1; row[nvar+bi] = -1
                    A2.append(row); rhs2.append(target[bi])
                    row = np.zeros(nvar+d); row[bi] = -1; row[nvar+bi] = -1
                    A2.append(row); rhs2.append(-target[bi])
                extra = linprog(np.r_[np.zeros(nvar), np.full(d, .5)], A_ub=A2, b_ub=rhs2,
                                A_eq=np.c_[eq, np.zeros((1, d))], b_eq=[1.0], bounds=(0, None), method='highs')
                assert extra.success, extra.message
                solves += 1
                vals.append(extra.fun)
            public_min += n/total*vals[0]
            null_min += vals[1]/(P//Q)**2
    assert residual < 1e-9
    row = dict(P=P, Q=Q, k=k, optimum=objective, conditional_LPs=len(grouped), solver_calls=solves,
                max_primal_residual=residual, elementary_bit_tuples=total,
                within_theorem=(Q >= 4 and Q % 2 == 0 and P//Q >= 3))
    if k == 2 and row['within_theorem']:
        row.update(min_public_among_strong_optima=public_min, min_null_among_strong_optima=null_min,
                   lexicographic_feasibility_allowance=1e-12)
    return row

def main():
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument("--out",type=Path,required=True); args=ap.parse_args()
    if args.out.exists(): raise SystemExit("Choose a fresh output path.")
    args.out.parent.mkdir(parents=True,exist_ok=True)
    params = [(12, 4, k) for k in range(1, 5)]+[(16, 4, 2), (16, 4, 3), (18, 6, 2), (18, 6, 3), (24, 8, 3), (6, 2, 2), (8, 4, 2)]
    rows = [solve(*p) for p in params]
    data = dict(status='PASS', arithmetic='IEEE 754 / SciPy HiGHS', cases=rows,
                total_conditional_LPs=sum(r['conditional_LPs'] for r in rows),
                total_solver_calls=sum(r['solver_calls'] for r in rows))
    args.out.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))

if __name__ == '__main__':
    main()
