"""Exact finite corroboration of Part I; this is not a universal proof."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import platform


def tv(mu, nu):
    return sum((abs(mu.get(x, 0) - nu.get(x, 0))
                for x in mu.keys() | nu.keys()), F(0)) / 2


def marginal(law, indices):
    result = Counter()
    for point, mass in law.items():
        result[tuple(point[i] for i in indices)] += mass
    return result


def main():
    report = {"scope": "Finite exact checks of the examples in Part I, version 0.2",
              "python": platform.python_version(), "arithmetic": "integers and Fraction",
              "row_enumerations": [], "carry_laws": []}
    domains = [(4, 2, 1), (4, 2, 2), (6, 2, 2),
               (6, 3, 2), (8, 2, 2), (8, 4, 2)]
    for P, Q, m in domains:
        inputs = list(product(range(P), repeat=m))
        admissible = 0
        for a in product(range(P), repeat=m):
            for b in range(P):
                fibers = {}
                compatible = True
                for z in inputs:
                    y = tuple(x // Q for x in z)
                    t = ((sum(c*x for c, x in zip(a, z)) + b) % P) // Q
                    if y in fibers and fibers[y] != t:
                        compatible = False
                        break
                    fibers[y] = t
                nonzero = [c for c in a if c]
                normal_form = (not nonzero or
                               len(nonzero) == 1 and
                               ((nonzero[0] == 1 and b % Q == 0) or
                                (nonzero[0] == P-1 and b % Q == Q-1)))
                assert compatible == normal_form, (P, Q, a, b)
                admissible += compatible
        assert admissible == P + 2*m*(P//Q)
        report["row_enumerations"].append({"P": P, "Q": Q, "m": m,
            "affine_rows_checked": P**(m+1), "admissible": admissible,
            "check": "all full-input observation fibers, against the row normal form"})

    identities = 0
    for P, Q in [(4, 2), (6, 2), (6, 3), (12, 3)]:
        values = [-2, -1, 0, 1, P-1, P, P+1]
        for z in product(values, repeat=2):
            y = [(x % P)//Q for x in z]
            r = [(x % P) % Q for x in z]
            for a in product(range(-2, 3), repeat=2):
                for b in [-P-1, -1, 0, Q-1, P+1]:
                    lhs = ((sum(c*x for c, x in zip(a, z)) + b) % P)//Q
                    rhs = (sum(c*x for c, x in zip(a, y)) +
                           (sum(c*x for c, x in zip(a, r))+b)//Q) % (P//Q)
                    assert lhs == rhs, (P, Q, a, b, z)
                    identities += 1
    report["signed_carry_identity_cases"] = identities

    for Q in range(2, 21):
        counts = Counter((a+b)//Q for a, b in product(range(Q), repeat=2))
        p0, p1 = F(counts[0], Q*Q), F(counts[1], Q*Q)
        assert p0 == F(Q+1, 2*Q) and p1 == F(Q-1, 2*Q)
        # Compute disagreement from two independent remainder-pair draws.
        disagreements = sum(counts[c]*counts[d] for c in counts for d in counts if c != d)
        posterior_error = F(disagreements, Q**4)
        best_error = 1-max(p0, p1)
        assert posterior_error == F(Q*Q-1, 2*Q*Q)
        assert best_error == p1
        report["carry_laws"].append({"Q": Q, "pairs": Q*Q,
            "best_error": str(best_error), "posterior_joint_error": str(posterior_error)})

    hidden_real = {(0, 0): F(1, 2), (1, 1): F(1, 2)}
    hidden_fresh = {(s, t): F(1, 4) for s, t in product(range(2), repeat=2)}
    assert tv(hidden_real, hidden_fresh) == F(1, 2)
    parity_real = {(s, y, s ^ y): F(1, 4) for s, y in product(range(2), repeat=2)}
    parity_fresh = {x: F(1, 8) for x in product(range(2), repeat=3)}
    assert tv(parity_real, parity_fresh) == F(1, 2)
    for coordinates in [(0, 1), (0, 2), (1, 2)]:
        assert marginal(parity_real, coordinates) == marginal(parity_fresh, coordinates)
    report["hidden_bit_joint_tv"] = "1/2"
    report["parity_triple_joint_tv"] = "1/2"
    report["parity_pairwise_marginals_equal"] = True
    report["status"] = "PASS"
    out = Path(__file__).resolve().parents[1] / "verification_results.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "affine_rows_checked":
        sum(x["affine_rows_checked"] for x in report["row_enumerations"]),
        "signed_carry_identity_cases": identities, "carry_orders_checked": 19,
        "output": str(out)}, indent=2))


if __name__ == "__main__":
    main()
