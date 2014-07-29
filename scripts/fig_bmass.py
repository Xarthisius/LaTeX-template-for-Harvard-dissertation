#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import preamble
import matplotlib.pyplot as plt


MEARTH = 5.97e27
data = np.loadtxt('../data/table')

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.semilogy(data[:, 1], data[:, 5] / MEARTH, 'o-', label="$\\alpha=0.01$")
ax.semilogy(data[:, 1], data[:, 3] / MEARTH, 'o-', label="$\\alpha=0.05$")
ax.semilogy(data[:, 1], data[:, 4] / MEARTH, 'o-', label="$\\alpha=0.1$")
ax.set_xlim((120, 300))
ax.set_ylim((0.007, 10))
ax.set_xlabel("Czas [rok]")
ax.set_ylabel(u"Masa pyłu związanego grawitacyjnie $[\\textrm{M}_\oplus]$")
fig.tight_layout()
ax.legend(loc=4)
fig.savefig('../figures/bmass_vs_time.pdf')
