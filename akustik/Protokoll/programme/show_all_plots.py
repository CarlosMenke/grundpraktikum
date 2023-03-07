#! /usr/bin/env python
# -*- coding: utf-8 -*-

### Das Ziel dieses Programs ist es, alle Messdaten, mit der FFT und dem Peak im Frequenz bereich darzustellen.
### Wir haben es benutzt, um zu schauen, ob das finden des Peaks zu testen und die qualität der Daten zu überprüfen.
### Wenn SHOW_PLOTS auf True gesetzt ist, werden alle Plots angezeigt
### Zum abspeichern muss der name der Messung in der Liste plots eingetragen werden.

import matplotlib.pyplot as plt
from praktikum import analyse
from praktikum import cassy
from pylab import *
import re
import os

global SHOW_PLOTS
SHOW_PLOTS = False

def cassy_plot(datei: str, x: str, y: str):
    # Gut lesbare und ausreichend große Beschriftung der Achsen, nicht zu dünne Linien.
    plt.rcParams['font.size'] = 24.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['lines.linewidth'] = 2.0

    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)


    xsymbol = x.symbol
    xsymbol = xsymbol.replace('&D', '\Delta{}')
    mx = re.match(r'([\\{}\w^_]+)_([\w^_]+)', xsymbol)
    if mx:
        xstr = '$%s_\mathrm{%s}$' % mx.groups()
    else:
        xstr = '$%s$' % xsymbol
    if x.einheit:
        xstr += ' / %s' % x.einheit

    ysymbol = y.symbol
    ysymbol = ysymbol.replace('&D', '\Delta{}')
    my = re.match(r'([\\{}\w^_]+)_([\w^_]+)', ysymbol)
    if my:
        ystr = '$%s_\mathrm{%s}$' % my.groups()
    else:
        ystr = '$%s$' % ysymbol
    if y.einheit:
        ystr += ' / %s' % y.einheit

    plt.figure()
    plt.subplot(2,1,1)
    plt.errorbar(x.werte, y.werte)
    plt.title('Daten')
    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.title(datei)
    plt.grid()
     
     # Fourier-Transformation
    plt.subplot(2,1,2)
    freq_fft,amp_fft = analyse.fourier_fft(x.werte,y.werte)
    plt.plot(freq_fft,amp_fft,'.',color='red',label="FFT")
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
    plt.legend()

    #fpeak_fft = analyse.peakfinder_schwerpunkt(freq_fft,amp_fft)
    fpeak_fft = analyse.peak(freq_fft,amp_fft, 1000, 2000)
    plt.axvline(fpeak_fft,color='black')
    plt.title('Fourierspektrum' + ' fpeak = ' + str(fpeak_fft) + ' Hz')
    plt.xlim(0.,np.max(freq_fft))
    plt.ylim(0.,np.max(amp_fft) * 1.1)

    plt.show()


def save_plot(datei: str, x: str, y: str, plotname: str):
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.linewidth'] = 0.75
    plt.rcParams['lines.linewidth'] = 0.5

    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)


    xsymbol = x.symbol
    xsymbol = xsymbol.replace('&D', '\Delta{}')
    mx = re.match(r'([\\{}\w^_]+)_([\w^_]+)', xsymbol)
    if mx:
        xstr = '$%s_\mathrm{%s}$' % mx.groups()
    else:
        xstr = '$%s$' % xsymbol
    if x.einheit:
        xstr += ' / %s' % x.einheit

    ysymbol = y.symbol
    ysymbol = ysymbol.replace('&D', '\Delta{}')
    my = re.match(r'([\\{}\w^_]+)_([\w^_]+)', ysymbol)
    if my:
        ystr = '$%s_\mathrm{%s}$' % my.groups()
    else:
        ystr = '$%s$' % ysymbol
    if y.einheit:
        ystr += ' / %s' % y.einheit

    plt.figure()
    plt.xlim(0.,3.)
    plt.errorbar(x.werte, y.werte)
    plt.title('Daten')
    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.title(plotname)
    plt.grid()
    plt.savefig(plotname + "_plot.pdf")
   
def save_fft_plot(datei: str, x: str, y: str, plotname: str):
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.linewidth'] = 0.75
    plt.rcParams['lines.linewidth'] = 0.5
     
    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)
     
     # Fourier-Transformation
    freq_fft,amp_fft = analyse.fourier_fft(x.werte,y.werte)
    plt.plot(freq_fft,amp_fft,'.',markersize=3,color='olive',label="FFT")
    plt.xlabel('$f$ / Hz')
    plt.ylabel('U_A1 / V')
    plt.grid()
    plt.legend()

    #fpeak_fft = analyse.peakfinder_schwerpunkt(freq_fft,amp_fft)
    fpeak_fft = analyse.peak(freq_fft,amp_fft, 1000, 2000)
    plt.axvline(fpeak_fft,color='black')
    plt.title('Fourierspektrum' + ' fpeak = ' + str(round(fpeak_fft, 2)) + ' Hz')
    plt.xlim(0.,np.max(freq_fft))
    plt.ylim(0.,np.max(amp_fft) * 1.1)

    plt.savefig(plotname + "_fft_plot.pdf")
     
cassy_dir = "../../Messungen/"
plots = [ "Alu_Messung_01", "Kupfer_Messung_02", "Stahl_Messung_01", "Messing_Messung_01" ]
fft_plots = [ "Alu_Messung_01", "Kupfer_Messung_02", "Stahl_Messung_01", "Messing_Messung_01" ]
 
for filename in sorted(os.listdir(cassy_dir)):
    if filename.endswith((".labx")):
        if SHOW_PLOTS: cassy_plot(cassy_dir + filename, "t", "U_A1")
        for plot in plots:
            if plot in filename:
                save_plot(cassy_dir + filename, "t", "U_A1", plot)
        for plot in fft_plots:
            if plot in filename:
                save_fft_plot(cassy_dir + filename, "t", "U_A1", plot)
                 
                 
                 
                 
                 
