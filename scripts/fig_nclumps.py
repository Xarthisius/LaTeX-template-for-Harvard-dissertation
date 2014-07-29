#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import preamble
import matplotlib.pyplot as plt


data = np.loadtxt('../data/table')

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(data[:, 1], data[:, 8], 'o-', label="$\\alpha=0.01$")
ax.plot(data[:, 1], data[:, 6], 'o-', label="$\\alpha=0.05$")
ax.plot(data[:, 1], data[:, 7], 'o-', label="$\\alpha=0.1$")
ax.set_xlim((120, 300))
#ax.set_ylim((-1, 450))
ax.set_xlabel("Czas [rok]")
ax.set_ylabel(u"Liczba związanych grawitacyjnie obiektów")
fig.tight_layout()
ax.legend(loc=2)
fig.savefig('../figures/nclumps_vs_time.pdf')
