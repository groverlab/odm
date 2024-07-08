import numpy, sys, matplotlib.pyplot as plt, scipy.signal

data = numpy.loadtxt(sys.argv[1], skiprows=10, )
# plt.plot(data)
smooth = scipy.signal.savgol_filter(data, 20, 3)
fig, ax = plt.subplots(1, 1, figsize=(10, 3))
ax.plot(smooth)
# plt.yscale("log")
ax.set_xlim(left=0, right=5.5e7)
ax.set_ylim(bottom=6000, top=16000)
plt.title(sys.argv[1])
fig.tight_layout()
fig.savefig(sys.argv[1]+".png")
plt.show()
