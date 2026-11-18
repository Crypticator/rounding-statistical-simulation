#!/usr/bin/env python3
"""Rebuild PDF, LaTeX, and HTML from the independent Markdown manuscript."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent.parent
stem='Affine_Maps_Modular_Rounding'
if (root/'scripts/build_figure.py').exists():
    subprocess.run([sys.executable,str(root/'scripts/build_figure.py')],check=True,cwd=root)
subprocess.run([sys.executable,str(root/'scripts/build_pdf.py')],check=True,cwd=root)
for extension,extra in [('tex',[]),('html',['--mathml'])]:
    subprocess.run(['pandoc',stem+'.md','--standalone','-o',stem+'.'+extension,*extra],check=True,cwd=root)
