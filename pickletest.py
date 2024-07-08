import bz2
import gzip
import lzma
import pickle
import numpy, sys

data = numpy.loadtxt(sys.argv[1], skiprows=10, )

# with open('aaa_no_compression.pickle', 'wb') as f:
#     pickle.dump(data, f)

# with gzip.open("aaa_gzip_test.gz", "wb") as f:
#     pickle.dump(data, f)

with bz2.BZ2File('aaa_bz2_test.pbz2', 'wb') as f:
    pickle.dump(data, f)

# with lzma.open("aaa_lzma_test.xz", "wb") as f:
#     pickle.dump(data, f)
