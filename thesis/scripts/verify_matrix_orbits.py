#!/usr/bin/env python3
"""Exact finite checks: direct row-path search versus orbit counting.

Standard Python only. Existing output is never overwritten. No delivered JSON
is read. Enumeration is an explicit finite verification, not an efficient
cryptographic reduction or a proof of the general theorems.
"""
import argparse
import itertools as it
import json
import math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


def rows(flat, m, n):
    return tuple(tuple(flat[i*n:(i+1)*n]) for i in range(m))


def neg(row, p):
    return tuple((-x) % p for x in row)


def key(a, p):
    return tuple(sorted(min(r, neg(r, p)) for r in a))


def size(k, p):
    d = Counter(k)
    v = math.factorial(len(k))
    for r, count in d.items():
        v //= math.factorial(count)
    return v * 2**sum(count for r, count in d.items() if r != neg(r, p))


def toeplitz(a):
    return all(a[i][j] == a[i-1][j-1]
               for i in range(1, len(a)) for j in range(1, len(a[0])))


def has_toeplitz_by_path(a, p):
    """Independent test: a signed ordering of all rows with matching overlaps."""
    m = len(a)
    choices = [tuple(dict.fromkeys((r, neg(r, p)))) for r in a]

    def visit(last, used):
        if used == (1 << m) - 1:
            return True
        for i in range(m):
            if used & (1 << i):
                continue
            for r in choices[i]:
                if last is None or r[1:] == last[:-1]:
                    if visit(r, used | (1 << i)):
                        return True
        return False
    return visit(None, 0)


def target_counts(p, m, n):
    c = Counter()
    for t in it.product(range(p), repeat=m+n-1):
        a = tuple(tuple(t[i-j+n-1] for j in range(n)) for i in range(m))
        assert toeplitz(a)
        c[key(a, p)] += 1
    return c


def delta_at(alpha, target, p, m, n):
    den, tden = p**(m*n), p**(m+n-1)
    return sum((max(F(0), F(c, tden)-F(size(k, p), den)/alpha)
                for k, c in target.items()), F(0))


def verify_domain(p, m, n):
    target = target_counts(p, m, n)
    dense = Counter()
    direct_hits = 0
    for flat in it.product(range(p), repeat=m*n):
        a = rows(flat, m, n)
        k = key(a, p)
        dense[k] += 1
        direct = has_toeplitz_by_path(a, p)
        assert direct == (k in target), (p, a, direct)
        direct_hits += direct
    for k, count in dense.items():
        assert count == size(k, p), (k, count, size(k, p))
    den, tden = p**(m*n), p**(m+n-1)
    d = (m-1)*(n-1)
    h = 2**(m-1)*math.factorial(m)
    saturated = sum(dense[k] for k in target)
    assert saturated == direct_hits
    assert F(saturated, den) <= min(F(1), F(h, p**d))
    for k, count in target.items():
        assert dense[k] <= h*count  # Orbitwise quotient by global negation.
    tv_orbits = sum((abs(F(count, den)-F(target[k], tden))
                     for k, count in dense.items()), F(0))/2
    assert tv_orbits == delta_at(F(1), target, p, m, n)
    if p**d >= h:
        assert tv_orbits == 1-F(saturated, den)
    acceptance = min(F(dense[k]*tden, den*count) for k, count in target.items())
    assert acceptance == F(1, p**d)
    zero = tuple((0,)*n for _ in range(m))
    assert dense[zero] == target[zero] == 1
    alphas = sorted({acceptance, min(F(1), 2*acceptance), F(1,4), F(1,2), F(3,4), F(1)})
    curve = [{'acceptance':str(a), 'optimal_tv':str(delta_at(a,target,p,m,n))}
             for a in alphas]
    assert curve[0]['optimal_tv'] == '0'
    return {
        'P':p, 'm':m, 'n':n, 'dense_matrices':den,
        'toeplitz_matrices':tden, 'source_orbits':len(dense),
        'target_orbits':len(target), 'direct_success_count':direct_hits,
        'orbit_success_count':saturated,
        'max_probability_toeplitz':str(F(saturated,den)),
        'union_bound':str(min(F(1),F(h,p**d))),
        'optimal_tv_without_rejection':str(tv_orbits),
        'support_lower_bound':str(1-F(saturated,den)),
        'exact_uniform_acceptance':str(acceptance),
        'acceptance_error_curve':curve,
        'target_orbit_profile':[{'canonical_rows':k, 'orbit_size':dense[k], 'target_count':c}
                                for k,c in sorted(target.items())],
    }


def mutations():
    a = ((1,0),(2,3))
    assert not has_toeplitz_by_path(a,8)
    aa = tuple(tuple(sum(a[i][k]*a[k][j] for k in range(2)) % 8
                     for j in range(2)) for i in range(2))
    assert aa == ((1,0),(0,1)) and toeplitz(aa)
    t = ((0,1),(2,0))
    assert toeplitz(t) and t[0][1] != t[1][0]
    # Forgetting the reflection shift fails for quotient cells.
    assert (0//2)==(1//2) and ((-0)%4)//2 != ((-1)%4)//2
    for x in range(4):
        assert ((-x+1)%4)//2 == (-(x//2)) % 2
    return {'column_change':{'P':8,'A':a,'V':a,'AV':aa},
            'toeplitz_not_hankel':t,'reflection_without_shift':'FAIL_AS_EXPECTED'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
    path=Path(args.out)
    if path.exists(): raise SystemExit('Refusing an existing output file')
    domains=[(4,2,2),(4,2,3),(4,3,2),(4,3,3),(8,2,2)]
    result={'status':'PASS','arithmetic':'integers and fractions.Fraction',
            'domains':[verify_domain(*v) for v in domains],'mutations':mutations()}
    result['dense_matrices_checked']=sum(d['dense_matrices'] for d in result['domains'])
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':result['status'],'dense_matrices_checked':result['dense_matrices_checked'],
                     'domains':[{k:v for k,v in d.items() if k not in ('target_orbit_profile','acceptance_error_curve')}
                                for d in result['domains']]},indent=2))


if __name__=='__main__': main()
