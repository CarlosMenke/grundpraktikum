#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:11:50 2023

@author: andrea
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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

def cassy_plot_clear(datei: str, x: str, y: str, plotname, end):
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
    plt.title(plotname)
    plt.plot(x.werte[:end], y.werte[:end],color='blue')
    plt.xlabel(xstr)
    plt.ylabel(ystr)
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname + '.pdf', bbox_inches='tight')
        

def cassy_plot(datei: str, x: str, y: str, plotname, show_peak):
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
    plt.title(plotname)
    freq_fft,amp_fft = analyse.fourier_fft(x.werte,y.werte)
    plt.plot(freq_fft,amp_fft,'.',color='red')
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'_fft_complete.pdf', bbox_inches='tight')
        
     # Fourier-Transformation mit Gezoomtem Intervall
    delta_2 = 50
    freq_fft,amp_fft = analyse.fourier_fft(x.werte,y.werte)
    f = np.max(amp_fft)
    a = np.where(amp_fft == f)[0][0]
    plt.figure()
    plt.title(plotname)
    plt.plot(freq_fft[a-delta_2:a+delta_2],amp_fft[a-delta_2:a+delta_2],'.',color='red')
    if show_peak:
        plt.axvline(freq_fft[a],color='green', label="peak")
        plt.legend()
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'_fft_small_zoom.pdf', bbox_inches='tight')
        
    
    plt.figure()
    plt.title(plotname)
    delta = 3
    plt.plot(freq_fft[a-delta:a+delta],amp_fft[a-delta:a+delta],'.',color='red')
    if show_peak:
        plt.axvline(freq_fft[a],color='green', label="peak")
        plt.legend()
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'_fft_zoom.pdf', bbox_inches='tight')
    return freq_fft[a]

def f_max(datei: str, x: str, y: str):
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

    freq_fft,amp_fft = analyse.fourier_fft(x.werte,y.werte)
    f = np.max(amp_fft)
    a = np.where(amp_fft == f)[0][0]
    return a
 
def plot_fpeak_errorbar(y, yerr, mean, plotname):
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.linewidth'] = 0.75
    plt.rcParams['lines.linewidth'] = 0.5
    plt.rcParams['savefig.pad_inches'] = 1
     
    fig, ax = plt.subplots()
    plt.errorbar(range(1, len(y)+1), y, yerr=yerr, fmt='.', markersize=8, capsize=2, capthick=0.8, elinewidth=1.5, label = "f_peak mit Fehler")
    plt.ylabel("Frequenzen / Hz")
    plt.autoscale()
    formatter = ticker.ScalarFormatter(useOffset=False)
    ax.yaxis.set_major_formatter(formatter)
    plt.title("Errorbar der Eigenfrequenz von Schwingkreis 2")
    ax.yaxis.set_label_coords(-0.2,0.50)
    plt.plot(range(1, len(y)+1), mean*np.ones(len(y)), linewidth = 1.5, label = "Mittelwert")
    plt.savefig("../plots/Errorbar_Tau_CASSY.pdf", bbox_inches='tight')
 
peak = []
plots = ['schwingkreis_2_01', 'schwingkreis_1_01', 'schwingkreis-alt-test-200us-0.01s']

for filename in sorted(os.listdir(cassy_dir)):
    if '.labx' in filename:
        if SHOW_PLOTS:
            cassy_plot(cassy_dir + filename, "t", "U_A1", filename[:-5])
 
cassy_plot(cassy_dir + plots[0] + '.labx', "t", "U_A1", plots[0], False)
cassy_plot(cassy_dir + plots[1] + '.labx', "t", "U_B1", plots[1], True)
cassy_plot(cassy_dir + plots[2] + '.labx', "t", "U_A1", plots[2], False)
         
cassy_plot_clear(cassy_dir + 'schwingkreis_1_01.labx', 't', 'U_B1', 'schwingkreis_1_01', -1)
cassy_plot_clear(cassy_dir + 'schwingkreis_1_01.labx', 't', 'U_B1', 'schwingkreis_1_01_zoom', 300)
cassy_plot_clear(cassy_dir + 'schwingkreis_2_01.labx', 't', 'U_A1', 'schwingkreis_2_01', -1)
cassy_plot_clear(cassy_dir + 'schwingkreis_2_01.labx', 't', 'U_A1', 'schwingkreis_2_01_zoom', 300)
 
# read in data
for filename in sorted(os.listdir(cassy_dir)):
    if 'schwingkreis_2' in filename:
        peak.append(f_max(cassy_dir + filename, "t", "U_A1"))

freq_peak = np.array(peak)

f_mean = np.mean(freq_peak)
f_stad = np.std(freq_peak, ddof=1)
plot_fpeak_errorbar(freq_peak, f_stad * np.ones(len(freq_peak)), f_mean, 'f_peak')

print('Mittelwert der Frequenzen', f_mean)
print('Standartabweichung der Einzelwerte', f_stad)

 
def get_messdaten(datei: str, y: str):
    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    y = messung.datenreihe(y)
    return np.array(y.werte)

def cassy_hist(datei: str, x: str, y: str, plotname: str):
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

    plt.figure()
    plt.title(plotname)
    plt.subplot(2,1,1)
    plt.hist(y.werte, bins = 100)
    plt.xlabel("U / V")
    plt.ylabel('Anzahl')
    plt.title(plotname)
    plt.tight_layout()
    
    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname + '.pdf', bbox_inches = 'tight')
 
cassy_hist('../Messdaten/rauschen_6V_01.labx', 't', 'U_A1', 'rauschen_6V_01')
rauschen_6 = get_messdaten('../Messdaten/rauschen_6V_01.labx', 'U_A1')
rauschen_0 = get_messdaten('../Messdaten/rauschen_0V_01.labx', 'U_A1')
