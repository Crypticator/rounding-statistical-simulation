#!/usr/bin/env python3
"""Rebuild finite evidence in a fresh directory; fail on any failed check."""
from pathlib import Path
import argparse,subprocess,sys,json
from verify_noise_channels import classify_domain

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--skip-lp',action='store_true');args=ap.parse_args()
    out=Path(args.out).resolve()
    out.mkdir(parents=True,exist_ok=False)
    classification=classify_domain(16)
    (out/'classification.json').write_text(json.dumps(dict(status='PASS',arithmetic='exact rational elimination',classification=classification),indent=2)+'\n')
    print(json.dumps({'classification_cases':classification['cases'],'rank_checks':classification['full_column_rank_checks']}),flush=True)
    here=Path(__file__).resolve().parent
    for script,name in [('verify_noise_metrics.py','metrics.json')]+([] if args.skip_lp else [('check_noise_lp.py','lp.json')]):
        subprocess.run([sys.executable,str(here/script),'--out',str(out/name)],check=True)
    print('All requested finite checks passed.',flush=True)

if __name__=='__main__':main()
