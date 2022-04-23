from ligotools.utils import whiten, write_wavfile, reqshift, plot_helper
import numpy as np
from scipy.interpolate import interp1d
from ligotools import readligo as rl
import os
import matplotlib.pyplot as plt
import matplotlib

def test_whiten():
	freqs = np.arange(0, 5, 0.25)
	pxx = np.arange(500, 505, 0.25)
	strain = np.arange(10, 70, 2)
	psd_temp = interp1d(freqs, pxx)
	whitened = whiten(strain, psd_temp, 100)
	assert isinstance(whitened, np.ndarray) == True

def test_write_wavfile():
	filepath = "audio/test.wav"
	bp = np.arange(0.4,0.8,0.02)
	write_wavfile(filepath, 5000, bp)
	assert os.path.exists(filepath)
	os.remove(filepath)

def test_reqshift():
	strain = np.arange(500, 1000,6)
	fshift = 400
	fs = 5000
	shifted_strain = reqshift(strain, fshift, fs)
	assert isinstance(shifted_strain, np.ndarray) == True

def test_plot_helper():
	make_plots = 1
	det = "L1"
	time = np.arange(1000,5000, 2)
	timemax = 5000
	SNR = np.arange(1, 5, 0.002)
	template_match = np.arange(1, 5, 0.002)
	eventname = "temp"
	plottype = 'png'
	tevent = 2502
	template_fft = np.arange(1020,5020, 2)
	datafreq = np.arange(1, 5, 0.002)
	d_eff = 100
	freqs = np.random.uniform(1, 40, 400)
	data_psd = np.arange(2000, 4000, 5)
	strain_H1_whitenbp = np.random.uniform(1, 500, 2000)
	fs = 4000
	strain_L1_whitenbp = np.random.uniform(1, 500, 2000)
	matplotlib.use('Agg')
	plot_helper(make_plots, det, time, timemax, SNR, template_match, eventname, plottype, tevent, 
					  template_fft, datafreq, d_eff, freqs, data_psd, strain_H1_whitenbp, fs, 
					  strain_L1_whitenbp)
	assert os.path.exist("data/" + eventname + "_" + det + "matchfreq." + plottype)
	assert os.path.exist("data/" + eventname + "_" + det + "matchtime." + plottype)
	assert os.path.exist("data/" + eventname + "_" + det + "SNR." + plottype)
	os.remove("data/" + eventname + "_" + det + "matchfreq." + plottype)
	os.remove("data/" + eventname + "_" + det + "matchtime." + plottype)
	os.remove("data/" + eventname + "_" + det + "SNR." + plottype)