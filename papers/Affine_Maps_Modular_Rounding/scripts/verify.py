#!/usr/bin/env python3
"""Exact exhaustive checks, standard-library Python only.

Run: python3 scripts/verify.py --out fresh/exact_results.json
Finite checks supplement the symbolic proofs; no security estimate is made.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, argparse


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def rounded(z, p, q):
    return tuple((x % p)//q for x in z)


def is_classified(u, b, p, q):
    nz = [a for a in u if a]
    return (not nz or (len(nz) == 1 and
            ((nz[0] == 1 and b % q == 0) or
             (nz[0] == p-1 and b % q == q-1))))


def affine_classification():
    rows = evaluations = witnesses = 0
    cases = []
    for p in range(4, 13):
        for q in range(2, p):
            if p % q:
                continue
            for m in (1, 2, 3):
                if m == 3 and p > 6:
                    continue
                good = 0
                zs = [(z, rounded(z, p, q)) for z in product(range(p), repeat=m)]
                for u in product(range(p), repeat=m):
                    for b in range(p):
                        fibers, factorizes = {}, True
                        for z, y in zs:
                            t = ((dot(u, z)+b) % p)//q
                            if y in fibers and fibers[y] != t:
                                factorizes = False
                            fibers[y] = t
                            evaluations += 1
                        expected = is_classified(u, b, p, q)
                        assert factorizes == expected, (p, q, m, u, b)
                        if factorizes:
                            sign_u = tuple(-1 if a == p-1 else a for a in u)
                            for y, t in fibers.items():
                                assert t == (dot(sign_u, y)+b//q) % (p//q)
                        else:
                            # An independent collision search in the zero cell
                            # supplies a concrete counterexample for EVERY row.
                            samples = [(r, (dot(u,r)+b) % p // q)
                                       for r in product(range(q), repeat=m)]
                            first = samples[0][1]
                            assert any(t != first for _, t in samples)
                            witnesses += 1
                        good += factorizes
                        rows += 1
                expected_count = p + 2*m*(p//q)
                assert good == expected_count
                cases.append(dict(P=p, Q=q, m=m, tested_rows=p**(m+1),
                                  factorizable_rows=good))
    return dict(affine_rows=rows, evaluated_points=evaluations,
                collision_witnesses=witnesses, cases=cases)


def carry_identity():
    count = 0
    for p in range(4, 17):
        for q in range(2,p):
            if p % q:
                continue
            for u in product(range(-2,3), repeat=2):
                for b in (-p-1, -1, 0, q-1, p+1):
                    for z in product(range(-p,p+1), repeat=2):
                        y = rounded(z,p,q)
                        r = tuple((x % p) % q for x in z)
                        t = ((dot(u,z)+b) % p)//q
                        derived = (dot(u,y) + (dot(u,r)+b)//q) % (p//q)
                        assert t == derived
                        count += 1
    return count


def sharp_prediction_loss():
    cases=[]
    for q in range(2,17):
        for k in (2,3,4):
            p=q*k
            joint=Counter()
            for z in product(range(p),repeat=2):
                joint[rounded(z,p,q), ((sum(z)%p)//q)] += 1
            best=Counter()
            for (y,t),n in joint.items():
                best[y]=max(best[y],n)
            loss=1-F(sum(best.values()),p*p)
            assert loss==F(q-1,2*q)
            # A simulator drawing the conditional carry has the exact (Y,T)
            # marginal, but its (Z,T) joint law has a different distance.
            c0,c1=F(q+1,2*q),F(q-1,2*q)
            for (y,t),n in joint.items():
                carry=(t-sum(y))%k
                assert carry in (0,1)
                assert F(n,p*p)==F(1,k*k)*(c1 if carry else c0)
            posterior_success = F(0)
            for z in product(range(p), repeat=2):
                y = rounded(z,p,q)
                t = (sum(z) % p)//q
                posterior_success += F(joint[y,t], q*q) / (p*p)
            posterior_joint_tv=1-posterior_success
            assert posterior_joint_tv==2*c0*c1
            assert posterior_joint_tv >= loss
            cases.append(dict(P=p,Q=q,K=k,optimal_error=str(loss),
                              public_posterior_TV='0',
                              posterior_Z_T_TV=str(posterior_joint_tv)))
    return cases


def scope_checks():
    count=0
    for p in range(4,17):
        for q in range(2,p):
            if p%q:
                continue
            k=p//q
            for z in range(-p,p+1):
                assert ((-z-1)%p)//q == k-1-((z%p)//q)
                count+=1
            for u in product(range(p),repeat=2):
                for y in product(range(k),repeat=2):
                    z=tuple(q*x for x in y)
                    assert (dot(u,z)%p)//q == dot(u,y)%k
                    count+=1
    # Binary-secret example: same public input, target reveals the secret.
    assert rounded((0,0),4,2)==rounded((1,1),4,2)==(0,0)
    assert rounded((0,0),4,2)==(0,0)
    assert rounded((2,1),4,2)==(1,0)
    # Any simulator on these two target outcomes has joint TV exactly 1/2.
    for i in range(101):
        p=F(i,100)
        distance=(abs(F(1,2)-F(1,2)*(1-p))+abs(F(1,2)*p)
                  +abs(F(1,2)*(1-p))+abs(F(1,2)-F(1,2)*p))/2
        assert distance==F(1,2)
    return dict(reflection_and_restricted_support_checks=count,
                binary_secret_probability_grid=101,
                binary_secret_minimum_joint_TV='1/2')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out",type=Path,required=True); args=ap.parse_args()
    if args.out.exists(): raise SystemExit("Choose a fresh output path.")
    args.out.parent.mkdir(parents=True,exist_ok=True)
    result=dict(status='PASS', scope='Exact affine and prediction checks; no security estimate',
                affine_classification=affine_classification(),
                carry_identity_checks=carry_identity(),
                sharp_prediction_loss=sharp_prediction_loss(),
                scope_checks=scope_checks())
    args.out.write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in
          ('affine_classification','sharp_prediction_loss')},indent=2))
    print('Affine classification:', {k:v for k,v in result['affine_classification'].items() if k!='cases'})
    print('Prediction laws:',len(result['sharp_prediction_loss']))


if __name__=='__main__':
    main()
