import numpy as np

def Ave_RMS(data):
    return np.nanmean(data), np.nanstd(data)