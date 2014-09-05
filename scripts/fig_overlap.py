#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import preamble
import matplotlib.pyplot as plt

data = np.loadtxt('../data/overlap.dat')

data[:, 1] /= data[:, 1].max()

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(data[:, 0], data[:, 1])
ax.set_xlim(2, 7)
ax.set_ylim(-0.05, 1.05)
ax.set_xlabel(r"$R$ [AU]")
ax.set_ylabel(r"$f(R)$")
plt.draw()
plt.savefig('../figures/overlap.pdf', bbox_inches="tight")
