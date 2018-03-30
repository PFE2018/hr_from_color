from pybdf import bdfRecording
import pandas as pd
import numpy as np
from matplotlib import pyplot
from biosppy import ecg

import matplotlib as ml
import matplotlib.pyplot as plt


#bdfRec = bdfRecording("../Dataset/Sessions/789/Part_7_N_Trial5_emotion.bdf")
bdfRec = bdfRecording("789/Part_7_N_Trial5_emotion.bdf")
ECG_idx = bdfRec.dataChanLabels.index('EXG2')
rec = bdfRec.getData(channels=[ECG_idx])
sampling_rate = bdfRec.sampRate[ECG_idx]
signal = np.array(rec['data'][0])
rec_s = pd.Series(rec['data'][0])
rec_s.plot()
pyplot.pause(0.1)

hr = ecg.ecg(signal=signal, sampling_rate=sampling_rate, show=False)[6]

#Must figure out a better way to find the time table.
#Video is 22 seconds and there is 85 samples
#video_duration = 22
#step = video_duration/float(len(hr))

step = 1/(float(sampling_rate)/60)
length = len(hr)
video_duration = step * float(len(hr))
time_array = np.arange(0, video_duration, step)

time_array_len = len(time_array)

combined = np.vstack((time_array, hr)).T
np.savetxt("ecg.csv", combined, delimiter=",")

hr = ecg.ecg(signal=signal, sampling_rate=sampling_rate, show=True)[6]

print('noice')
