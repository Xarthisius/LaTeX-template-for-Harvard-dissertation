#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import matplotlib
matplotlib.use('pgf')


FILES = [
    'dend_proj_kepler_tst_0075.h5.npy',
    'dend_proj_kepler_tst_0100.h5.npy',
    'dend_proj_kepler_tst_0126.h5.npy',
    'dend_proj_kepler_tst_0146.npy'
]

matplotlib.rcParams['font.size'] = 16
preamble = {
    'text.usetex': True,
    "pgf.rcfonts": False,
    "text.latex.unicode": True,
    "pgf.preamble": [
        r"\usepackage[T1]{polski}",
        r"\usepackage{mathspec}",
        r"\setmathsfont(Digits,Latin,Greek)[Numbers={OldStyle,Proportional}]{Arno Pro}",
        r"\setmathrm{Arno Pro}",
    ]
}
matplotlib.rcParams.update(preamble)

from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 9))

grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(4, 1),
                 direction="column",
                 axes_pad=0.05,
                 label_mode="L",
                 share_all=True,
                 cbar_location="right",
                 cbar_mode="single",
                 cbar_size="1%",
                 cbar_pad="1%")

for ifn, fn in enumerate(FILES):
    data = np.load(fn)
    data *= 8483.30609653
    vmax = 0.12 * 8483.30609653
    im = grid[ifn].imshow(data, interpolation='nearest',
                          vmin=0.0, vmax=vmax, cmap='Greys',
                          extent=[2.5, 6.0, 0.0, 0.52])
    grid[ifn].yaxis.set_major_locator(MaxNLocator(5, prune="both"))
    grid[ifn].set_ylabel("$\\varphi$")

grid[-1].set_xlabel("$R$ [AU]")
grid[-1].cax.colorbar(im)
grid[-1].cax.set_ylabel(u"Gęstość kolumnowa [g/cm$^2$]", rotation=90)
grid[-1].cax.toggle_label(True)
fig.savefig('../figures/proj_sg.pdf', bbox_inches="tight")
