import matplotlib.pyplot as plt
import sys, numpy, scipy.signal
from scipy.signal import find_peaks, medfilt
from scipy.stats import iqr

data = numpy.loadtxt(sys.argv[1], skiprows=10)
smooth = scipy.signal.savgol_filter(data, 20, 3)
# smooth = data
smooth = -smooth + 16000

peaks, properties = find_peaks(smooth, prominence=50)
print(peaks)
print(len(peaks))

# plt.plot(smooth)
plt.plot(peaks, smooth[peaks], ".", markersize=0.5, color="k")
plt.plot(peaks, medfilt(smooth[peaks], 1001), "-")

plt.gca().set_yscale("log")
plt.title(sys.argv[1])
# plt.show()
plt.savefig(sys.argv[1] + "_PEAKS.pdf")

