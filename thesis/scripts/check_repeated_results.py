#!/usr/bin/env python3
"""Cross-check separate exact and LP runs; check explicit constants and domains."""
from pathlib import Path
from fractions import Fraction as F
import json, platform
import scipy, numpy, matplotlib, reportlab
from verify_repeated import optimum_formula
from sample_repeated import sample_optimal
import random

import argparse
ap=argparse.ArgumentParser(); ap.add_argument("--directory",type=Path,required=True); args=ap.parse_args()
root=args.directory
exact = json.loads((root/'exact_results.json').read_text())
lp = json.loads((root/'lp_results.json').read_text())
differences = []
for case in lp['cases']:
    delta = abs(case['optimum']-float(optimum_formula(case['Q'], case['k'])))
    if case['within_theorem']:
        assert delta < 1e-9
        differences.append(delta)
        if case['k'] == 2:
            assert abs(case['min_public_among_strong_optima']-1/(8*case['Q'])) < 1e-9
            assert abs(case['min_null_among_strong_optima']-5/(6*(case['P']//case['Q']))) < 1e-9
    else:
        assert delta > 1e-3

for case in exact['cases']:
    if case['k'] == 2:
        Q, L = case['Q'], case['P']//case['Q']
        balanced = F(case['optimal_public'])+F(case['optimal_null'])
        fair = F(case['fair_public'])
        assert (balanced > fair) == (3*L < 8*Q)
for P, Q in ((8, 4), (6, 2), (15, 5)):
    try:
        sample_optimal((0, 1), P, Q, random.Random(0))
    except ValueError:
        pass
    else:
        raise AssertionError('Invalid model accepted')
data = dict(status='PASS', exact_cases=exact['enumeration_cases'], noise_tuples=exact['noise_tuples'],
            LP_cases=len(lp['cases']), conditional_LPs=lp['total_conditional_LPs'],
            total_solver_calls=lp['total_solver_calls'],
            in_domain_LP_cases=len(differences), negative_domain_controls=2,
            max_formula_LP_difference=max(differences),
            python=platform.python_version(), scipy=scipy.__version__, numpy=numpy.__version__,
            matplotlib=matplotlib.__version__, reportlab=reportlab.Version,
            limitations=['Finite enumeration corroborates but does not prove the general theorem.',
                         'LP checks use floating point; mathematical proof is in the manuscript.',
                         'These calculations make no cryptographic security claim.'])
(root/'validation.json').write_text(json.dumps(data, indent=2)+'\n')
print(json.dumps(data, indent=2))
