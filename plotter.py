import numpy, sys, matplotlib.pyplot as plt, scipy.signal

data = numpy.loadtxt(sys.argv[1], skiprows=10, )
stat = open(sys.argv[1][:-8]+"STAT.txt").read()
start = float(stat.split("\n")[0])
stop = float(stat.split("\n")[1])
duration = stop-start
points = len(data)
times = numpy.linspace(0, duration, points)
smooth = scipy.signal.savgol_filter(data, 20, 3)
# smooth=data
fig, ax = plt.subplots(1, 1, figsize=(10, 3))
ax.plot(times, smooth)
# plt.yscale("log")
# ax.set_xlim(left=0, right=3.5e6)
# ax.set_ylim(bottom=13000, top=15500)
plt.title(sys.argv[1])
plt.xlabel("Time (s)")
plt.ylabel("Light intensity (arbitrary)")
fig.tight_layout()
fig.savefig(sys.argv[1]+".png")
plt.show()