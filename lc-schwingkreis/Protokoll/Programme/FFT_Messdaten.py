#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:11:50 2023

@author: andrea
"""

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
 
cassy_dir = "../Messdaten/"


def cassy_plot(datei: str, x: str, y: str, plotname, save):
    # Gut lesbare und ausreichend große Beschriftung der Achsen, nicht zu dünne Linien.
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['lines.linewidth'] = 2.0
    plt.rcParams["savefig.pad_inches"] = 0.5

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

    # Ungeschnittenen Fouriert
    plt.figure()
    freq_fft,amp_fft = analyse.fourier_fft(x.werte,y.werte)
    plt.plot(freq_fft,amp_fft,'.',color='red',label="FFT")
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
    plt.legend()
     
    if SHOW_PLOTS and not save:
        plt.show()
    elif not SHOW_PLOTS and save:
        plt.savefig('../plots/' +plotname +'_complete.pdf', bbox_inches='tight')
        
     # Fourier-Transformation mit Gezoomtem Intervall
    delta_2 = 50
    freq_fft,amp_fft = analyse.fourier_fft(x.werte,y.werte)
    f = np.max(amp_fft)
    a = np.where(amp_fft == f)[0][0]
    plt.figure()
    plt.plot(freq_fft[a-delta_2:a+delta_2],amp_fft[a-delta_2:a+delta_2],'.',color='red',label="FFT")
    plt.axvline(freq_fft[a],color='green')
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
    plt.legend()
     
    if SHOW_PLOTS and not save:
        plt.show()
    elif not SHOW_PLOTS and save:
        plt.savefig('../plots/' +plotname +'_small_zoom.pdf', bbox_inches='tight')
        
    
    plt.figure()
    delta = 3
    plt.plot(freq_fft[a-delta:a+delta],amp_fft[a-delta:a+delta],'.',color='red',label="FFT")
    plt.axvline(freq_fft[a],color='green')
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
    plt.legend()
    if SHOW_PLOTS and not save:
        plt.show()
    elif not SHOW_PLOTS and save:
        plt.savefig('../plots/' +plotname +'_zoom.pdf', bbox_inches='tight')
    return freq_fft[a]

def cassy_hist(datei: str, x: str, y: str):
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.labelweight'] = 'normal'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['lines.linewidth'] = 1.0
    plt.rcParams["savefig.pad_inches"] = 0.5
    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)
    
    b = 2000
    plt.figure()
    plt.plot(x.werte[1:b], y.werte[1:b])
    plt.xlabel('t in s')
    plt.ylabel('U in v')
    plt.figure()
    plt.hist(y.werte, bins = 100)
    plt.xlabel("U / V")
    plt.ylabel('Anzahl')
    plt.tight_layout()
    plt.grid()
    

peak = []
plots = ['schwingkreis_2_01', 'alt-test-50us.labx']

for filename in sorted(os.listdir(cassy_dir)):
    if '.labx' in filename:
        if SHOW_PLOTS:
            cassy_plot(cassy_dir + filename, "t", "U_A1", filename[:-5], False)
        else:
            for plot in plots:
                if plot in filename:
                    cassy_plot(cassy_dir + filename, "t", "U_A1", filename[:-5], True) 
         
# read in data
for filename in sorted(os.listdir(cassy_dir)):
    if 'schwingkreis_2' in filename:
        f_peak = cassy_plot(cassy_dir + filename, "t", "U_A1", filename[:-5], False)
        peak.append(f_peak)

freq_peak = np.array(peak)

f_mean = np.mean(freq_peak)
f_stad = np.std(freq_peak, ddof=1)

print('Mittelwert der Frequenzen', f_mean)
print('Standartabweichung der Einzelwerte', f_stad)

#cassy_hist('../Messdaten/rauschen_0V_01.labx', 't', 'U_A1')
#cassy_hist('../Messdaten/rauschen_6V_01.labx', 't', 'U_A1')


#cassy_plot('../Messdaten/schwingkreis_1_01.labx', 't', 'U_B1')
