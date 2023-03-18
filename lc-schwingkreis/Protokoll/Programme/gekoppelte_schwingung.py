#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from praktikum import analyse
from praktikum import cassy
import pandas as pd
from pylab import *
import os
import cassy_helper as ch

global SHOW_PLOTS
SHOW_PLOTS = False #for debugging, zeige alle Messdaten und die Fouriertrasformierte mit peak an.
 
global PLOTS_DIR #Ordner, in dem die Plots gespeichert werden sollen, mit passender Martrikelnummer und Versuchnummer
PLOTS_DIR = '../plots/434170_428396_1A3_'
 
cassy_dir = "../Messdaten/"


def cassy_plot_clear(datei: str, x: str, y: str, plotname, end):
    x, y, xstr, ystr = ch.cassy_begin(datei, x, y)
    # Ungeschnittenen Fouriert
    plt.figure()
    plt.title(plotname)
    plt.plot(x.werte[:end], y.werte[:end],color='blue')
    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.grid()
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname + '.pdf', bbox_inches='tight')
         
def cassy_plot_fft(datei: str, x_str: str, y_str: str, plotname, delta, peak):
    x, y, _, _ = ch.cassy_begin(datei, x_str, y_str)
    # Ungeschnittenen Fouriert
    extension = ""
     
    a = ch.f_max(datei, x_str, y_str)[0]
    freq_fft,amp_fft = analyse.fourier_fft(x.werte,y.werte)
     
    plt.figure()
    plt.title(plotname)
    plt.plot(freq_fft[a-delta:a+delta],amp_fft[a-delta:a+delta],'.',color='blue')
    if peak: 
        plt.axvline(freq_fft[a],color='green', label="Maximum")
        plt.legend()
        extension = "_peak"
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'_fft_zoom' + extension + '.pdf', bbox_inches='tight')
         

for filename in sorted(os.listdir(cassy_dir)):
    if '.labx' in filename and 'sinnig' in filename:
        if SHOW_PLOTS:
            try:
                cassy_plot_clear(cassy_dir + filename, "t", "U_A1", filename[:-5], -1)
            except:
                cassy_plot_clear(cassy_dir + filename, "t", "U_B1", filename[:-5], -1)

cassy_plot_clear(cassy_dir + "gegensinnig_01" + ".labx", "t", "U_A1", "gegensinnig_01", 500)
cassy_plot_clear(cassy_dir + "gleichsinnig_01_spule_gedreht" + ".labx", "t", "U_A1", "gleichsinnig_01_spule", 500)
cassy_plot_clear(cassy_dir + "gleichsinnig_01_spannung_gedreht" + ".labx", "t", "U_A1", "gleichsinnig_01_spannung", 500)

cassy_plot_fft(cassy_dir + "gegensinnig_01" + ".labx", "t", "U_A1", "gegensinnig_01", 3, True)
cassy_plot_fft(cassy_dir + "gleichsinnig_01_spule_gedreht" + ".labx", "t", "U_A1", "gleichsinnig_01_spule", 3, True)
cassy_plot_fft(cassy_dir + "gegensinnig_01" + ".labx", "t", "U_A1", "gegensinnig_01", 50, False)
cassy_plot_fft(cassy_dir + "gleichsinnig_01_spule_gedreht" + ".labx", "t", "U_A1", "gleichsinnig_01_spule", 50, False)
