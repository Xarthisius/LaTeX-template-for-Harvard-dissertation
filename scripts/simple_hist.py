# This Python file uses the following encoding: utf-8
import numpy as np
import matplotlib

matplotlib.use('pgf')
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
#matplotlib.rcParams.update(preamble)


import matplotlib.pyplot as plt

a = np.loadtxt('all_mass.txt')
b = np.loadtxt('bound_mass.txt')
fig, ax = plt.subplots()
n, bins, patches = ax.hist(a, 30, normed=0, facecolor="0.65",
                           alpha=0.75, log=True, label=u"wszystkie")
#n, bins, patches = ax.hist(b, 30, normed=0, facecolor="red",
#                           alpha=1.0, log=True, label=u"związane")
ax.set_xlabel(r"Masa $[\textrm{M}_{\textrm{ceres}}$]")
ax.set_ylabel(u"Liczba obiektów")
#plt.legend()
#plt.draw()
plt.savefig('../figures/masshist.pgf')
