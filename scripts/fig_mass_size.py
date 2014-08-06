#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import preamble
import matplotlib.pyplot as plt

data = np.loadtxt('../data/mass_size_300.dat')
mass = data[:, 0]
Lp = data[:, 3]
Lxz = data[:, 4]
rho = data[:, 5]
# Plot data

fig = plt.figure(1, figsize=(14, 12))
ax = fig.add_subplot(221)
ax.loglog(mass, Lp, 'bo')
ax.set_xlabel(r'Masa obiektu $[\textrm{g}]$')
ax.set_ylabel(u'''Maksymalny rozmiar obiektu $[\\textrm{cm}]$''')
ax.set_ylim((2e11, 1e13))

ax = fig.add_subplot(222)
ax.loglog(rho, Lp, 'bo')
ax.set_xlabel(u'Gęstość średnia obiektu $[\\textrm{g}/\\textrm{cm}^3]$')
#ax.set_ylabel(u'''Maksymalny rozmiar obiektu $[\\textrm{cm}]$''')
ax.set_xlim((5e-9, 1.5e-8))
ax.set_ylim((2e11, 1e13))

ax = fig.add_subplot(223)
ax.loglog(mass, Lxz, 'bo')
ax.set_xlabel(r'Masa obiektu $[\textrm{g}]$')
ax.set_ylabel(u'Rozmiar obiektu w płaszczyźnie $(xz)\;[\\textrm{cm}]$')
ax.set_ylim((2e10, 1.5e12))

ax = fig.add_subplot(224)
ax.loglog(rho, Lxz, 'bo')
ax.set_xlabel(u'Gęstość średnia obiektu $[\\textrm{g}/\\textrm{cm}^3]$')
#ax.set_ylabel(u'Rozmiar obiektu w płaszczyźnie $(xz)\;[\\textrm{cm}]$')
ax.set_ylim((2e10, 1.5e12))
ax.set_xlim((5e-9, 1.5e-8))

plt.tight_layout()
plt.savefig('../figures/fig_mass_size.pdf')
