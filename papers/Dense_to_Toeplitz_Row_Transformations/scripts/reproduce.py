#!/usr/bin/env python3
"""Recompute results into a new directory; supplied data are never inputs."""
from pathlib import Path
import argparse,json,subprocess,sys,platform,importlib.metadata
root=Path(__file__).resolve().parent.parent
ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
out=args.out.resolve()
if out.exists():raise SystemExit('Choose a directory that does not yet exist.')
out.mkdir(parents=True)
commands=[['verify.py', 'exact_results.json'], ['check_lp.py', 'lp_results.json'], ['check_structure.py', 'structure_results.json']]
for script,result in commands:
    ans=subprocess.run([sys.executable,str(root/'scripts'/script),'--out',str(out/result)],capture_output=True,text=True)
    (out/(script+'.log')).write_text(ans.stdout+ans.stderr)
    if ans.returncode: raise SystemExit(ans.stdout+ans.stderr)
    print(script+': PASS',flush=True)
if (root/'scripts/check_results.py').exists():
    ans=subprocess.run([sys.executable,str(root/'scripts/check_results.py'),'--directory',str(out)],capture_output=True,text=True)
    (out/'check_results.log').write_text(ans.stdout+ans.stderr)
    if ans.returncode:raise SystemExit(ans.stdout+ans.stderr)
versions={'python':platform.python_version(),'platform':platform.platform()}
for name in ('numpy','scipy','matplotlib','reportlab','Pillow'):
    try: versions[name]=importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:pass
(out/'environment.json').write_text(json.dumps(versions,indent=2)+'\n')
print('All reproduction checks passed.')
