import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw = mne.io.read_raw_edf('aaaaaayx_s002_t000.edf', preload=True)
info = raw.info[0]
print(info)
# print(raw.ch_names())
# # raw.filter(1,20)

# raw.plot()

from pyedflib import highlevel
import pyedflib as plib
import numpy as np
import matplotlib.pyplot as plt

path = "aaaaaayx_s002_t000.edf"
signals, signal_headers, header = highlevel.read_edf(path)

# print(signals)

n = len(signals)

# fig = plt.figure(figsize=(150,50))
# ax = plt.axes()
# for i in np.arange(n):
#     ax.plot(signals[i] , color='purple' )
#     plt.show()