
import pyedflib
import numpy as np


def edf2nd(arq):
    f = pyedflib.EdfReader(arq)
    n = f.signals_in_file
    channels = f.getSignalLabels()
    signal = np.zeros((n, f.getNSamples()[0]))

    for i in np.arange(n):
        signal[i, :] = f.readSignal(i)

    return [channels,signal]