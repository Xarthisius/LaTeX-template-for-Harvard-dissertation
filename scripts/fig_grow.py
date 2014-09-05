import numpy as np
import cPickle as pickle
import preamble
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

FILES = [
    ('../data/sg_modes.pkl', '../figures/sg_vlzd_growth.pdf'),
    ('../data/nosg_modes.pkl', '../figures/nosg_vlzd_growth.pdf'),
]


def format_my(x, pos=None):
    return "%i" % np.log(x)


def save_my_plot(pklfile, outname):
    with open(pklfile, 'rb') as fh:
        data = pickle.load(fh)

    fig, axs = plt.subplots(nrows=2, ncols=3, sharex=True, figsize=(16, 12))
    fig.tight_layout()
    plt.subplots_adjust(wspace=0.08, hspace=0.08)
    for i, item in enumerate(data):
        ax = axs.ravel()[i]
        func_m, func_o, p, time_sim, kx, kz = item
        ax.plot(time_sim, func_m, '-', lw=1.5, c='0.45')
        ax.plot(time_sim, func_o, '--', lw=1.5, c='0.45')
        ax.plot(time_sim, p, lw=1.5, c='k')
        ax.set_ylim([np.e ** (-15.9), np.e ** (-8.1)])
        ax.set_yscale('log', basey=np.e)
        ax.yaxis.set_major_formatter(FuncFormatter(format_my))
        ax.xaxis.set_major_locator(MaxNLocator(6, prune="both"))
        # ax.xaxis.set_major_locator(FixedLocator([35,45,55,65]))
        if i > 2:
            ax.set_xlabel("t [rok]")
        if i % 3 == 0:
            ax.set_ylabel(r"$\ln \left(\delta w_z\right)$")
        else:
            ax.set_yticklabels([])
    plt.draw()
    fig.savefig(outname)

for pklfile, outname in FILES:
    save_my_plot(pklfile, outname)
