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
SHOW_PLOTS = False #for debugging, zeige alle Messdaten und die Fouriertrasformierte mit peak an.
 
global PLOTS_DIR #Ordner, in dem die Plots gespeichert werden sollen, mit passender Martrikelnummer und Versuchnummer
PLOTS_DIR = '../plots/434170_428396_1A3_'

def cassy_plot(datei: str, x: str, y: str):
    # Gut lesbare und ausreichend große Beschriftung der Achsen, nicht zu dünne Linien.
    plt.rcParams['font.size'] = 24.0
    plt.rcParams['font.family'] = 'sans-serif'
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
    start = start_values[plotname] if plotname in start_values else 0
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
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
    plt.xlim(start / 10000,3.)
    plt.errorbar(x.werte[start:], y.werte[start:])
    plt.title('Daten')
    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.title(plotname)
    plt.grid()
    plt.savefig(PLOTS_DIR + plotname + "_plot.pdf")
   
def save_fft_plot(datei: str, x: str, y: str, plotname: str, save_peak: bool = True):
    start = start_values[plotname] if plot in start_values else 0
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.linewidth'] = 0.75
    plt.rcParams['lines.linewidth'] = 0.5
     
    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)
     
     # Fourier-Transformation
    freq_fft,amp_fft = analyse.fourier_fft(x.werte[start:],y.werte[start:])
    plt.plot(freq_fft,amp_fft,'.',markersize=3,color='olive',label="FFT")
    plt.xlabel('$f$ / Hz')
    plt.ylabel('U_A1 / V')
    plt.grid()
    plt.legend()

    #fpeak_fft = analyse.peakfinder_schwerpunkt(freq_fft,amp_fft)
    if save_peak:
        fpeak_fft = analyse.peak(freq_fft,amp_fft, 1000, 2000)
        plt.axvline(fpeak_fft,color='black')
        plt.title('FFT ' + plotname + ' fpeak = ' + str(round(fpeak_fft, 2)) + ' Hz')
    else:
        plt.title('FFT ' + plotname)
    plt.xlim(0.5,np.max(freq_fft))
    plt.ylim(0.,np.max(amp_fft) * 1.1)

    plt.savefig(PLOTS_DIR + plotname + "_fft.pdf")
     
cassy_dir = "../../Messungen/"
plots = [ "Alu_Messung_01", "Alu_Messung_08", "Kupfer_Messung_02", "Kupfer_Messung_09", "_Kupfer_Messung_09", "Stahl_Messung_02", "Messing_Messung_01", "Kupfer_Einsp_Fehler_01", "_Kupfer_Einsp_Fehler_01", "Kupfer_Einsp_Fehler_05", "Alu_Messung_07"]
fft_plots_without_peak = [ "Alu_Messung_01", "Alu_Messung_08", "Kupfer_Messung_02", "Kupfer_Messung_09", "_Kupfer_Messung_09", "Stahl_Messung_02", "Messing_Messung_01" ]
fft_plots = ["Kupfer_Einsp_Fehler_01", "_Kupfer_Einsp_Fehler_01", "Kupfer_Einsp_Fehler_05", "Alu_Messung_07"]
global start_values # wenn der Messwert in diesem Dictionary steht, wird der Startwert für die Plots gesetzt welcher nicht 0 ist
start_values = {"Kupfer_Einsp_Fehler_01": 5000,
                "Kupfer_Messung_03":4500,
                "Kupfer_Messung_04":5000,
                "Kupfer_Messung_06":5000,
                "Kupfer_Messung_07":5000,
                "Kupfer_Messung_09":5000,
                "Messing_Messung_06":5000,
                "Messing_Messung_07":5000,
                "Stahl_Messung_01":2000,
                "Stahl_Messung_09":5000,
                } # Der Startwert / 10000 ergibt die Startsekunde
 
for filename in sorted(os.listdir(cassy_dir)):
    if filename.endswith((".labx")):
        if SHOW_PLOTS: cassy_plot(cassy_dir + filename, "t", "U_A1")
        for plot in plots:
            if plot in filename:
                save_plot(cassy_dir + filename, "t", "U_A1", plot)
        for plot in fft_plots_without_peak:
            if plot in filename:
                save_fft_plot(cassy_dir + filename, "t", "U_A1", plot, save_peak=False)
        for plot in fft_plots:
            if plot in filename:
                save_fft_plot(cassy_dir + filename, "t", "U_A1", plot)
