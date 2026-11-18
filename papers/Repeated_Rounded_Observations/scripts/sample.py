#!/usr/bin/env python3
"""Expected polynomial-time sampler for the explicit strong-optimal kernel.
The caller supplies fair random bits. The seeded CLI is only a reproducible demo.
All observations must be available before output; this is not an online sampler.
"""
import random

def third(rng):
    """Uniform integer in {0,1,2}, via rejection of 3."""
    while True:
        x = rng.getrandbits(2)
        if x < 3:
            return x

def sample_optimal(y, P, Q, rng):
    if Q < 4 or Q % 2 or P % Q or P//Q < 3 or not y:
        raise ValueError('Need even Q>=4, P=LQ, L>=3, k>=1')
    L = P//Q
    if any(not isinstance(v, int) or not 0 <= v < L for v in y):
        raise ValueError('Observations must lie in Z_L')
    cells = set(y)
    candidates = [(u, (u+1) % L) for u in cells if (u+1) % L in cells] if len(cells) == 2 else []
    if len(candidates) != 1:
        return tuple(rng.getrandbits(1) for _ in y)
    u, v = candidates[0]
    ell = y.count(u)
    left = bool(rng.getrandbits(1)) if 2*ell == len(y) else 2*ell > len(y)
    if left:
        return tuple(int(third(rng) < 2) if t == u else 0 for t in y)
    return tuple(1 if t == u else int(third(rng) == 0) for t in y)

if __name__ == '__main__':
    rng = random.Random(20261114)
    for y in ((0, 0, 0), (0, 1, 0), (3, 0), (0, 2), (0, 1, 2)):
        print(y, '->', sample_optimal(y, 16, 4, rng))
