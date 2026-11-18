#!/usr/bin/env python3
"""Check the delivered package's SHA-256 manifests using the standard library."""
from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parent.parent
manifests = [root / 'SHA256SUMS', root / 'thesis/SHA256SUMS']
manifests.extend(sorted((root / 'papers').glob('*/SHA256SUMS')))
failed = []
checked = 0
for manifest in manifests:
    if not manifest.is_file():
        failed.append(f'Missing manifest: {manifest.relative_to(root)}')
        continue
    for line in manifest.read_text().splitlines():
        if not line:
            continue
        expected, name = line.split('  ', 1)
        path = manifest.parent / name
        if not path.resolve().is_relative_to(root.resolve()):
            failed.append(f'Path outside package: {name}')
            continue
        checked += 1
        if not path.is_file():
            failed.append(f'Missing: {path.relative_to(root)}')
        elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            failed.append(f'Changed: {path.relative_to(root)}')
if failed:
    print('\n'.join(failed))
    sys.exit(1)
print(f'PASS: {checked} checksum entries in {len(manifests)} manifests.')
print('Integrity only: this does not verify mathematical correctness or peer review.')
