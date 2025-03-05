import matplotlib.pyplot as plt
import sys, numpy, scipy.signal
from scipy.signal import find_peaks, medfilt
from scipy.stats import iqr, gaussian_kde

data = numpy.loadtxt(sys.argv[1], skiprows=10)
smooth = scipy.signal.savgol_filter(data, 20, 3)
# smooth = data


baseline = numpy.median(smooth[0:int(len(smooth)/10)])

# smooth = -(smooth - 15120)
# smooth = -(smooth - 993)
smooth = -(smooth-baseline)

peaks, properties = find_peaks(smooth, prominence=20)  # was 50, then 20 for r4, then 5 for r3
print(peaks)
print(len(peaks))



# plt.plot(smooth)
# plt.plot(peaks, smooth[peaks], ".", markersize=5, color="r")
# # plt.plot(peaks, medfilt(smooth[peaks], 101), "b-")  # was 1001
# plt.show()
# exit()

plt.hist2d(peaks, smooth[peaks], [200, 100])
plt.show()
exit()

# plt.hist(peaks, bins=100)
# plt.gca().set_xlim(0, 3500000)
# # plt.gca().set_ylim(0, 120)
# plt.gca().set_xlabel("Time [s]")
# plt.gca().set_ylabel("Peak count")


# plt.gca().set_yscale("log")
plt.title(sys.argv[1])
# plt.show()
plt.savefig(sys.argv[1] + "_PEAKS.png")
# 
