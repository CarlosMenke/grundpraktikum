#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from praktikum import cassy
from praktikum import analyse
import numpy as np
import matplotlib.pyplot as plt

# Gut lesbare und ausreichend große Beschriftung der Achsen, nicht zu dünne Linien:
plt.rcParams['font.size'] = 24.0
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelsize'] = 'medium'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.linewidth'] = 1.2
plt.rcParams['lines.linewidth'] = 2.0

data = cassy.CassyDaten('lab/Pendel.lab')
timeValues = data.messung(1).datenreihe('t').werte
voltage = data.messung(1).datenreihe('U_A1').werte
voltageError = 0. * voltage + 0.01
offset = analyse.gewichtetes_mittel(voltage, voltageError)[0]
voltage = voltage - offset

plt.figure(1, figsize=(20,10))
plt.title('Pendel')

plt.subplot(2,1,1)
plt.plot(timeValues, voltage)
plt.grid()
plt.xlabel('Zeit / s')
plt.ylabel('Spannung / V')
einhuellende = analyse.exp_einhuellende(timeValues, voltage, voltageError)
plt.plot(timeValues, +einhuellende[0] * np.exp(-einhuellende[2] * timeValues))
plt.plot(timeValues, -einhuellende[0] * np.exp(-einhuellende[2] * timeValues))

plt.subplot(2,1,2)
fourier = analyse.fourier_fft(timeValues, voltage)
frequency = fourier[0]
amplitude = fourier[1]
plt.plot(frequency, amplitude)
plt.grid()
plt.xlabel('Frequenz / Hz')
plt.ylabel('Amplitude')

maximumIndex = amplitude.argmax();
plt.xlim(frequency[max(0, maximumIndex-10)], frequency[min(maximumIndex+10, len(frequency))])
peak = analyse.peakfinder_schwerpunkt(frequency, amplitude)
plt.axvline(peak)

L = 0.667
g = ((2 * np.pi * peak)**2) * L

print('g = %f m/s^2' % g)

plt.tight_layout()
plt.show()
