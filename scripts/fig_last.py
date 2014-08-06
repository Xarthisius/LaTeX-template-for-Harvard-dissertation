#!/usr/bin/env python
# encoding: utf-8

import preamble
import cPickle as pickle
import matplotlib.pyplot as plt

with open("../data/hist_nosg_300.pkl", 'r') as fh:
    x = pickle.load(fh)
    y = pickle.load(fh)
    z = pickle.load(fh)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.loglog(y, z[:, 29], label="R = %3.1f" % x[29])
ax.loglog(y, z[:, 79], label="R = %3.1f" % x[79])
ax.set_xlim((1e-12, 1e-9))
ax.set_ylim((1e-9, 1e-4))
ax.set_xlabel(u"Gęstość pyłu $[\\textrm{g}/\\textrm{cm}^3]$")
ax.set_ylabel(u"Masa pyłu $[\\textrm{M}_{\\textrm{jup}}]$")
fig.tight_layout()
ax.legend(loc=4)
fig.savefig('../figures/hist1d_nosg.pdf')

with open("../data/hist_sg_300.pkl", 'r') as fh:
    x = pickle.load(fh)
    y = pickle.load(fh)
    z = pickle.load(fh)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.loglog(y, z[:, 29], label="R = %3.1f" % x[29])
ax.loglog(y, z[:, 79], label="R = %3.1f" % x[79])
ax.set_xlim((1e-13, 3e-8))
ax.set_ylim((1e-8, 5e-4))
ax.set_xlabel(u"Gęstość pyłu $[\\textrm{g}/\\textrm{cm}^3]$")
ax.set_ylabel(u"Masa pyłu $[\\textrm{M}_{\\textrm{jup}}]$")
fig.tight_layout()
ax.legend(loc=4)
fig.savefig('../figures/hist1d_sg.pdf')
