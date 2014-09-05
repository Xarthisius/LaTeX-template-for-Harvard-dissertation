import numpy as np
import preamble
import matplotlib.pyplot as plt

y = np.loadtxt('../data/growthAB.dat')

fig = plt.figure(1, (8,6))
ax = fig.add_subplot(111)
ax.loglog(np.logspace(-1, 1, 100), np.array(y), lw=2)
ax.set_xlim([0.1, 10.0])
ax.set_ylim([1e-2, 0.3])
ax.set_xlabel(r"$\epsilon$")
ax.set_ylabel(r"$s/\Omega$")
plt.tight_layout()
plt.savefig("../figures/growthAB.pdf", facecolor="white", bbox_inches="tight")
