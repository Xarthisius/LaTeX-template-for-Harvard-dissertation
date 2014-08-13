import numpy as np
#import preamble
import matplotlib.pyplot as plt
from scipy import stats

data = np.loadtxt('../data/mass_size_300.dat')
mass = data[:, 0]
Lp = data[:, 3]
Lxz = data[:, 4]
rho = data[:, 5]
#ind = np.where(Lp < 1e13)
ind = np.where((Lxz < 2e12) & (Lxz > 0.0))
# Plot data

x = np.log10(Lxz[ind])
y = np.log10(mass[ind])
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print 'r value', r_value
print  'p_value', p_value
print 'standard deviation', std_err
print 'slope', slope
print 'intercept', intercept

fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111)
ax.plot(x, y, 'bo')
line = slope * x + intercept
ax.plot(x, line, '-', label="a = %4.2f +/- %4.2f" % (slope, std_err))
#ax.set_ylim((2e11, 1e13))
plt.show()
