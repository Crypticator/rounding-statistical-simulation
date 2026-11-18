#!/usr/bin/env python3
"""Check native equations and common LibreOffice formula-import defects.
This automatic check supplements, but does not replace, visual inspection.
Usage: python tools/check_document.py --docx FILE --pdf FILE [--expected-pages N]
Requires PyMuPDF for the PDF check; all DOCX checks use the standard library.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--docx',type=Path,required=True)
    ap.add_argument('--pdf',type=Path,required=True)
    ap.add_argument('--expected-pages',type=int)
    a=ap.parse_args()
    for p in (a.docx,a.pdf):
        if not p.is_file():ap.error(f'File not found: {p}')
    try:
        import fitz
    except ImportError as exc:
        raise SystemExit('Install PyMuPDF to check the rendered PDF.') from exc
    ns={'m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
    val='{'+ns['m']+'}val'
    with ZipFile(a.docx) as z:root=ET.fromstring(z.read('word/document.xml'))
    from collections import Counter
    issues=[];pluses=0
    blackboard=Counter()
    symbol_map={'Z':'ℤ','R':'ℝ','E':'𝔼'}
    for run in root.findall('.//m:r',ns):
        node=run.find('m:t',ns);text=node.text or '' if node is not None else ''
        style=run.find('m:rPr/m:scr',ns)
        if style is not None and style.get(val)=='double-struck' and text in symbol_map:
            blackboard[symbol_map[text]]+=1
        else:
            blackboard.update(c for c in text if c in symbol_map.values())
    pdf_text=[]
    for sub in root.findall('.//m:sub',ns):
        if ''.join(t.text or '' for t in sub.findall('.//m:t',ns))=='+':
            pluses+=1
            literal=sub.find('.//m:lit',ns)
            if literal is None or literal.get(val)!='1':issues.append('Nonliteral standalone positive-part subscript')
    for sep in root.findall('.//m:sepChr',ns):
        if sep.get(val)=='':issues.append('Empty optional equation delimiter separator')
    with fitz.open(a.pdf) as d:
        pages=len(d)
        for i,p in enumerate(d,1):
            text=p.get_text();pdf_text.append(text)
            for mark in ('¿','�','<?>'):
                if mark in text:issues.append(f'Page {i}: possible formula import defect {mark!r}')
    combined=''.join(pdf_text)
    for symbol,count in blackboard.items():
        if combined.count(symbol)!=count:issues.append(f'Double-struck symbol {symbol}: expected {count}, extracted {combined.count(symbol)}; inspect export')
    if a.expected_pages is not None and pages!=a.expected_pages:issues.append(f'Expected {a.expected_pages} pages; found {pages}')
    result={'status':'FAIL' if issues else 'PASS','pdf_pages':pages,'native_math_objects':len(root.findall('.//m:oMath',ns)),'positive_part_subscripts':pluses,'double_struck_symbols':dict(blackboard),'issues':issues,'limit':'Visual inspection is still required; this is not mathematical proof checking.'}
    print(json.dumps(result,indent=2))
    if issues:raise SystemExit(1)
if __name__=='__main__':main()
