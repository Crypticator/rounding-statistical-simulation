#!/usr/bin/env python3
"""Reproduce author checks for Chapters 7–8 in a new output directory."""
from pathlib import Path
import argparse,subprocess,sys

ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--skip-lp',action='store_true');a=ap.parse_args()
out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
here=Path(__file__).resolve().parent
jobs=[('verify_matrix_orbits.py','orbits.json',[]),
      ('check_matrix_extensions.py','extensions.json',['--skip-lp'] if a.skip_lp else [])]
if not a.skip_lp:jobs.append(('check_matrix_lp.py','matrix_lp.json',[]))
for script,name,extra in jobs:
    subprocess.run([sys.executable,str(here/script),'--out',str(out/name),*extra],check=True)
print('All requested Part III checks passed.')
