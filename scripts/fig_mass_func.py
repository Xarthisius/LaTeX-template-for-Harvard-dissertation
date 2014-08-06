#/usr/bin/env python
# encoding: utf-8

import numpy as np
import preamble
import h5py as h5
import matplotlib.pyplot as plt

data = {}
with h5.File('../data/histograms.h5', 'r') as fh:
    for dset in fh.keys():
        data[dset] = fh[dset][:].copy()


nbins = 41
min_bin = 1.0
max_bin = 800.0

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

times = np.array(map(float, data.keys()))
for time in times[times >= 250.0]:
    hist, bin_edges = np.histogram(data["%5.1f" % time][:, 0],
                                   bins=np.logspace(0, 3, nbins))
    hist, bin_edges = np.histogram(data["%5.1f" % time][:, 0],
                                   bins=np.linspace(0.0, 800, nbins))

    centers = (bin_edges + np.roll(bin_edges, 1)) * 0.5
    ax.loglog(centers[1:], hist, 'rx')

x = np.logspace(1.0, 1e3, 50)

ax.plot(x, 6e3 * x ** -1.25, label=r"$\propto x^{-1.25\pm0.12}$")
ax.plot(x, 1e7 * x ** (-8./3.), label=r"$\propto x^{-\frac{8}{3}}$")
ax.set_xlim((5, 1e3))
ax.set_ylim((0.9, 200))
ax.set_xlabel("Masa obiektu $[\\textrm{M}_{\\textrm{ceres}}]$")
ax.set_ylabel(u"Liczba obiektów")
plt.legend(loc=3)
fig.tight_layout()
plt.savefig('../figures/mass_func.pdf')
