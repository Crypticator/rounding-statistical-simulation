#!/usr/bin/env python3
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from verify import optimum_formula, fair_formula

root = Path(__file__).resolve().parent.parent
ks = list(range(1, 33))
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
fig, ax = plt.subplots(figsize=(8.2, 3.65), layout='constrained')
ax.plot(ks, [float(optimum_formula(4, k)) for k in ks], color='#155d87', lw=2.2, label='Optimal block simulation')
ax.plot(ks, [float(fair_formula(4, k)) for k in ks], color='#b95321', lw=2.2, label='Independent fair bits')
ax.axhline(.5, color='#777777', linestyle='--', lw=.9)
ax.text(32, .507, 'Fair-bit limit: 2/Q = 1/2', ha='right', fontsize=9, color='#555555')
ax.set(xlabel='Number of observations k (shared state Z)', ylabel='Total variation of (Z, Y, B)', xlim=(1, 32), ylim=(0, .55))
ax.set_xticks([1, 4, 8, 12, 16, 20, 24, 28, 32])
ax.grid(alpha=.2)
ax.legend(loc='center right', frameon=False, fontsize=9)
for ext in ('png', 'pdf', 'svg'):
    fig.savefig(root/'figures'/('block_simulation.'+ext), dpi=180)
plt.close(fig)
