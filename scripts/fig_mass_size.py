#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import preamble
import matplotlib.pyplot as plt

data = np.loadtxt('../data/mass_size_300.dat')
x = data[:, 0] * 8.958e23
# Plot data

fig = plt.figure(1, figsize=(14, 6))
ax = fig.add_subplot(121)
ax.loglog(x, data[:, 3], 'bo')
ax.set_xlabel(r'Masa obiektu $[\textrm{g}]$')
ax.set_ylabel(u'''Maksymalny rozmiar obiektu $[\\textrm{cm}]$''')
ax = fig.add_subplot(122)
ax.loglog(x, data[:, 4], 'bo')
# ax.set_xlabel(r'Masa obiektu $[\textrm{M}_{\textrm{ceres}}]$')
ax.set_xlabel(r'Masa obiektu $[\textrm{g}]$')
ax.set_ylabel(u'Rozmiar obiektu w płaszczyźnie $(xz)\;[\\textrm{cm}]$')
plt.tight_layout()
plt.savefig('../figures/fig_mass_size.pdf')
