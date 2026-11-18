#!/usr/bin/env python3
"""Direct finite checks of cell rigidity and Toeplitz/Hankel orbit equivalence.

Standard library only. No scientific script or delivered data is imported.
These finite computations corroborate, rather than prove, the general results.
"""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import product, permutations
from math import factorial, gcd
from pathlib import Path
import json


def row_factorizes(coefficients, b, p, q):
    outputs = {}
    for x in product(range(p), repeat=len(coefficients)):
        observed = tuple(v // q for v in x)
        value = ((sum(a*v for a, v in zip(coefficients, x)) + b) % p) // q
        if observed in outputs and outputs[observed] != value:
            return False
        outputs[observed] = value
    return True


def row_classification(coefficients, b, p, q):
    nonzero = [a for a in coefficients if a]
    return (not nonzero or
            len(nonzero) == 1 and
            ((nonzero[0] == 1 and b % q == 0) or
             (nonzero[0] == p-1 and b % q == q-1)))


def scalar_checks():
    domains = []
    for p in range(4, 25):
        for q in range(2, p):
            if p % q:
                continue
            admitted = 0
            for a, b in product(range(p), repeat=2):
                first_cell = len({((b+a*r) % p)//q for r in range(q)}) == 1
                full = row_factorizes((a,), b, p, q)
                predicted = row_classification((a,), b, p, q)
                assert first_cell == full == predicted, (p, q, a, b)
                admitted += full
            domains.append({'P': p, 'Q': q, 'cases': p*p, 'admitted': admitted})
    return domains


def row_checks():
    domains = []
    parameters = [(4, 2, 2), (4, 2, 3)]
    parameters += [(p, q, 2) for p in (6, 8, 9, 10, 12)
                   for q in range(2, p) if p % q == 0]
    for p, q, dimension in parameters:
        count = admitted = 0
        for coefficients in product(range(p), repeat=dimension):
            for b in range(p):
                actual = row_factorizes(coefficients, b, p, q)
                assert actual == row_classification(coefficients, b, p, q), (p, q, coefficients, b)
                count += 1
                admitted += actual
        domains.append({'P': p, 'Q': q, 'dimension': dimension,
                        'cases': count, 'admitted': admitted})
    return domains


def matrix_factorizes(u, b, p, q):
    outputs = {}
    for x in product(range(p), repeat=2):
        observed = tuple(v//q for v in x)
        value = tuple(((sum(u[i][j]*x[j] for j in range(2)) + b[i]) % p)//q
                      for i in range(2))
        if observed in outputs and outputs[observed] != value:
            return False
        outputs[observed] = value
    return True


def matrix_checks():
    domains = []
    for p, q in [(4, 2), (6, 2), (6, 3)]:
        count = admitted = matrices = 0
        for a, b, c, d in product(range(p), repeat=4):
            if gcd(a*d-b*c, p) != 1:
                continue
            u = ((a, b), (c, d))
            matrices += 1
            for shift in product(range(p), repeat=2):
                actual = matrix_factorizes(u, shift, p, q)
                predicted = all(row_classification(u[i], shift[i], p, q) for i in range(2))
                assert actual == predicted, (p, q, u, shift)
                if predicted:
                    columns = [next(j for j in range(2) if u[i][j]) for i in range(2)]
                    assert columns[0] != columns[1]
                count += 1
                admitted += actual
        domains.append({'P': p, 'Q': q, 'dimension': 2,
                        'invertible_matrices': matrices,
                        'matrix_translation_cases': count, 'admitted': admitted})
    return domains


def images(a, p):
    m = len(a)
    return {tuple(tuple(signs[i]*v % p for v in a[ordering[i]]) for i in range(m))
            for ordering in permutations(range(m))
            for signs in product((-1, 1), repeat=m)}


def orbit_size_formula(a, p):
    types = Counter(min(r, tuple(-v % p for v in r)) for r in a)
    denominator = 1
    occurrences = 0
    for r, count in types.items():
        denominator *= factorial(count)
        if r != tuple(-v % p for v in r):
            occurrences += count
    return factorial(len(a)) // denominator * 2**occurrences


def is_toeplitz(a):
    return all(a[i][j] == a[i-1][j-1]
               for i in range(1, len(a)) for j in range(1, len(a[0])))


def is_hankel(a):
    return all(a[i][j] == a[i-1][j+1]
               for i in range(1, len(a)) for j in range(len(a[0])-1))


def structure_checks():
    results = []
    for p, m, n in [(4, 2, 2), (4, 2, 3), (4, 3, 2), (4, 3, 3), (8, 2, 2)]:
        toeplitz_profile, hankel_profile = Counter(), Counter()
        sizes = {}
        count = 0
        for sequence in product(range(p), repeat=m+n-1):
            t = tuple(tuple(sequence[i-j+n-1] for j in range(n)) for i in range(m))
            h = tuple(tuple(sequence[i+j] for j in range(n)) for i in range(m))
            assert is_toeplitz(t) and is_hankel(h)
            reversed_t = tuple(reversed(t))
            assert is_hankel(reversed_t) and is_toeplitz(tuple(reversed(h)))
            ot, oh = images(t, p), images(h, p)
            assert ot == images(reversed_t, p)
            assert len(ot) == orbit_size_formula(t, p)
            assert len(oh) == orbit_size_formula(h, p)
            kt, kh = min(ot), min(oh)
            toeplitz_profile[kt] += 1
            hankel_profile[kh] += 1
            sizes[kt], sizes[kh] = len(ot), len(oh)
            count += 1
        assert toeplitz_profile == hankel_profile
        N, target_size, d = p**(m*n), p**(m+n-1), (m-1)*(n-1)
        support_success = sum(Fraction(sizes[k], N) for k in toeplitz_profile)
        distances = []
        for alpha in sorted({Fraction(1, p**d), Fraction(1, 2), Fraction(1)}):
            delta_t = sum((max(Fraction(0), Fraction(c, target_size)-Fraction(sizes[k], N)/alpha)
                           for k, c in toeplitz_profile.items()), Fraction(0))
            delta_h = sum((max(Fraction(0), Fraction(c, target_size)-Fraction(sizes[k], N)/alpha)
                           for k, c in hankel_profile.items()), Fraction(0))
            assert delta_t == delta_h
            distances.append({'acceptance': str(alpha), 'common_optimal_tv': str(delta_t)})
        exact_acceptance = min(Fraction(sizes[k]*target_size, N*c)
                               for k, c in toeplitz_profile.items())
        assert exact_acceptance == Fraction(1, p**d)
        results.append({'P': p, 'm': m, 'n': n,
                        'matrices_per_target_support': count,
                        'target_orbits': len(toeplitz_profile),
                        'target_orbit_masses_equal': True,
                        'common_support_success': str(support_success),
                        'common_exact_acceptance': str(exact_acceptance),
                        'common_distance_curve': distances})
    return results


def stabilizer_controls():
    cases = [
        (4, ((0, 2), (0, 2), (2, 0))),
        (4, ((1, 0), (1, 0), (3, 0))),
        (4, ((0, 0), (1, 2), (3, 2))),
        (8, ((0, 4), (0, 4), (4, 0))),
        (8, ((1, 2), (1, 2), (7, 6))),
    ]
    result = []
    for p, a in cases:
        actual = len(images(a, p))
        assert actual == orbit_size_formula(a, p)
        result.append({'P': p, 'rows': a, 'orbit_size': actual})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    if args.out.exists():
        raise SystemExit('Refusing an existing output file')
    result = {'status': 'PASS', 'arithmetic': 'integers and fractions.Fraction',
              'scalar_cell_domains': scalar_checks(),
              'affine_row_domains': row_checks(),
              'invertible_affine_matrix_domains': matrix_checks(),
              'toeplitz_hankel_domains': structure_checks(),
              'stabilizer_controls': stabilizer_controls()}
    result['counts'] = {
        'scalar_cell_cases': sum(x['cases'] for x in result['scalar_cell_domains']),
        'affine_row_cases': sum(x['cases'] for x in result['affine_row_domains']),
        'invertible_matrix_translation_cases': sum(x['matrix_translation_cases'] for x in result['invertible_affine_matrix_domains']),
        'target_matrices_enumerated': 2*sum(x['matrices_per_target_support'] for x in result['toeplitz_hankel_domains']),
        'explicit_stabilizer_controls': len(result['stabilizer_controls'])}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': result['status'], 'counts': result['counts']}, indent=2))


if __name__ == '__main__':
    main()
