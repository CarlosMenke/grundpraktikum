#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:52:24 2023

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

def Plot_begin_2(datei: str, x: str, y: str, datei_2: str, y_2: str):
    plt.rcParams['font.size'] = 14.0
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

    data = cassy.CassyDaten(datei_2)
    messung = data.messung(1)
    y_2 = messung.datenreihe(y_2)
     
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
    
    return x.werte, y.werte, y_2.werte, xstr, ystr
    
f_1 = 61
f_2 = 71

T_1 = 1/f_1
T_2 = 1/f_2

def cassy_plot_clear_2(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, start, end):
    
    x, y, y_2, xstr, ystr = Plot_begin_2(datei, x, y, datei_2, y_2)
    f_1 = 61
    f_2 = 71

    T_1 = 1/f_1
    T_2 = 1/f_2
    # Ungeschnittenen Fouriert
    plt.figure()
    plt.title(plotname)
    
    plt.plot(x[start:end], y[start:end], color='blue',  label='Schwingkreis 1')
    plt.plot(x[start:end], y_2[start:end], color='magenta', label='Schwingkreis 2')
    plt.plot(x[start:end], np.sin((T_1/50+x[start:end])/T_1*(np.pi*2))*5.98*np.exp((-1)*x[start:end]*149.43), color = 'orange')
    plt.plot(x[start:end], (-1)*np.sin((T_1/50+x[start:end])/T_1*(np.pi*2))*5.98*np.exp((-1)*x[start:end]*149.43), color = 'orange')
    plt.plot(x[start:end], np.cos((x[start:end]-T_2/40)/T_2*(np.pi*2))*5.8863*np.exp((-1)*x[start:end]*160.03), color = 'green')
    plt.plot(x[start:end], (-1)*np.cos((x[start:end]-T_2/40)/T_2*(np.pi*2))*5.8863*np.exp((-1)*x[start:end]*160.03), color = 'green')
    plt.xlabel(xstr)
    plt.legend()
    plt.ylabel(ystr)
    plt.grid()
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname + '.pdf', bbox_inches='tight')

def cassy_plot_clear_2_c(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, start, end):
    
    x, y, y_2, xstr, ystr = Plot_begin_2(datei, x, y, datei_2, y_2)
    plt.rcParams['font.weight'] = 'normal'
    plt.figure()
    plt.title(plotname)
    
    plt.plot(x[start:end], y[start:end],'.', color='blue',  label='Schwingkreis 1')
    plt.plot(x[start:end], y_2[start:end],'.', color='magenta', label='Schwingkreis 2')
    plt.axvline(x[57]+0.00003, color ='cyan')
    plt.axvline(x[75]+0.00001, color = 'cyan')
    plt.xlabel(xstr)
    plt.legend()
    plt.ylabel(ystr)
    plt.grid()
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname + '.pdf', bbox_inches='tight')


f = 61
k = 0.094
R = 2.690
L = (9.02*10**(-3))
C = (2.301*10**(-6))
delt_t = 1/(2*np.pi*f)*(1/np.pi-np.arctan(k/R*np.sqrt(L/C)))
print(delt_t+0.004)
 
def cassy_plot_clear_2_max(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, start, end):
    
    x, y, y_2, xstr, ystr = Plot_begin_2(datei, x, y, datei_2, y_2)
    plt.rcParams['font.weight'] = 'normal'
    plt.figure()
    plt.title(plotname)
    
    plt.plot(x[start:end], y[start:end],'.', color='blue',  label='Schwingkreis 1')
    plt.plot(x[start:end], y_2[start:end],'.', color='magenta', label='Schwingkreis 2')
    plt.axvline(x[57]+0.00003, color ='cyan')
    #plt.axvline(x[75]+0.00001, color = 'cyan')
    plt.xlabel(xstr)
    plt.legend()
    plt.ylabel(ystr)
    plt.grid()
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname + '.pdf', bbox_inches='tight')

cassy_plot_clear_2('../Messdaten/Schwebung_0cm_01.labx','t', 'U_B1', '../Messdaten/Schwebung_0cm_01.labx', 'U_A1', 'Schwebung_0cm_01_Delta_T', 0, 250 )
cassy_plot_clear_2_c('../Messdaten/Schwebung_0cm_01.labx','t', 'U_B1', '../Messdaten/Schwebung_0cm_01.labx', 'U_A1', 'Schwebung_0cm_01_Delta_T_zoom', 55, 79 )
cassy_plot_clear_2_max('../Messdaten/Schwebung_0cm_01.labx','t', 'U_B1', '../Messdaten/Schwebung_0cm_01.labx', 'U_A1', 'Schwebung_0cm_01_Delta_T_Max', 55, 61 )


