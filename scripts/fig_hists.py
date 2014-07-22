#!/usr/bin/env python
# encoding: utf-8

import matplotlib
import cPickle as pickle
matplotlib.use('pgf')


FILES = [
    '../data/hist_nosg_050.pkl',
    '../data/hist_sg_050.pkl',
    '../data/hist_nosg_100.pkl',
    '../data/hist_sg_100.pkl',
    '../data/hist_nosg_200.pkl',
    '../data/hist_sg_200.pkl',
    '../data/hist_nosg_300.pkl',
    '../data/hist_sg_300.pkl',
]

preamble = {
    'text.usetex': True,
    "pgf.rcfonts": False,
    "text.latex.unicode": True,
    'font.size': 22,
    "pgf.preamble": [
        r"\usepackage[T1]{polski}",
        r"\usepackage{mathspec}",
        r"\setmathsfont(Digits,Latin,Greek)[Numbers={OldStyle,Proportional}]{Arno Pro}",
        r"\setmathrm{Arno Pro}",
    ]
}
matplotlib.rcParams.update(preamble)

from matplotlib.ticker import MaxNLocator
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=4, ncols=2, sharex=True, sharey=True,
                        figsize=(12, 18))
plt.subplots_adjust(wspace=0.06, hspace=0.08, right=0.83)

for ifn, fn in enumerate(FILES):
    grid = axs.ravel()[ifn]
    with open(fn, 'r') as fh:
        x = pickle.load(fh)
        y = pickle.load(fh)
        z = pickle.load(fh)

    vmin = 1e-9  # np.nanmin(vals[used_bin])
    vmax = 1e-3  # np.nanmax(vals[used_bin])
    norm = LogNorm(vmin=vmin, vmax=vmax, clip=False)

    grid.set_yscale("log")
    grid.set_xlim(2.5, 6.0)
    grid.set_ylim(1e-14, 1e-7)
    im = grid.pcolormesh(
        x, y, z, shading='flat', rasterized=True, norm=norm, cmap="YlOrBr",
    )
    grid.xaxis.set_major_locator(MaxNLocator(8, prune="both"))
for grid in axs[:, 0]:
    grid.set_ylabel(r"$\varrho_{\textrm{D}}$ [g/cm${^3}$]")
for grid in axs[-1, :]:
    grid.set_xlabel(r"$R$ [AU]")

cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
cax = fig.colorbar(im, cax=cbar_ax)
cbar_ax.set_xlabel("$\;\;\;\;\;M_\\textrm{D}$ [M$_{\\textrm{jup}}$]", labelpad=20)
fig.savefig('../figures/hists2d.pdf', bbox_inches="tight")
