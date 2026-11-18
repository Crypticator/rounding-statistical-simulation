#!/usr/bin/env python3
"""Rebuild the new chapter checks into a fresh output directory."""
from pathlib import Path
import argparse,subprocess,sys
ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--skip-lp',action='store_true');args=ap.parse_args()
out=args.out.resolve();out.mkdir(parents=True,exist_ok=False)
here=Path(__file__).resolve().parent
jobs=[('verify_repeated.py','exact_results.json',[]),('verify_two_worlds.py','two_worlds.json',['--skip-lp'] if args.skip_lp else [])]
if not args.skip_lp: jobs.append(('check_repeated_lp.py','lp_results.json',[]))
for script,name,extra in jobs:
    subprocess.run([sys.executable,str(here/script),'--out',str(out/name),*extra],check=True)
if not args.skip_lp:
    subprocess.run([sys.executable,str(here/'check_repeated_results.py'),'--directory',str(out)],check=True)
print('All requested Part IV checks passed.')
