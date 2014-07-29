#!/usr/bin/env python
# encoding: utf-8

import preamble
import cPickle as pickle

FILES = [
    '../data/a296.dat',
    '../data/b296.dat',
    '../data/c296.dat',
]

from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True,
                        figsize=(16, 6))
plt.subplots_adjust(wspace=0.06, hspace=0.08, right=0.83)

zoom = [2.5, 3, 6]

for ifn, fn in enumerate(FILES):
    grid = axs[ifn]
    data = np.loadtxt(fn)

    n, bins, patches = grid.hist(data[:, 0], bins=np.linspace(0, 600, 31))
    grid.set_xlabel(r"Masa obiektu $[\textrm{M}_{\textrm{ceres}}]$")
    grid.xaxis.set_major_locator(MaxNLocator(8, prune="lower"))
    axins = zoomed_inset_axes(grid, zoom[ifn], loc=1)
    n, bins, patches = axins.hist(data[data[:, 0] <= 80.0, 0],
                                  bins=np.linspace(0,80,21))
    axins.xaxis.set_major_locator(MaxNLocator(4, prune="lower"))
    mark_inset(grid, axins, loc1=3, loc2=4, fc="none", ec="0.5")

ax = axs[0]
ax.set_ylabel(u"Liczba związanych obiektów")
fig.savefig('../figures/mass_hists.pdf', bbox_inches="tight")
