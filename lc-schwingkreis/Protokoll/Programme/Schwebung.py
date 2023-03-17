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

# Dieser Teil des Programms Erstellt aus den Gemessenen Spannungen an Kondensator 1 und Kondensator 2 einen Plot in welchem diese gemeinsam sind
def cassy_plot_clear_2(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, end):
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['lines.linewidth'] = 0.8
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

    # Ungeschnittenen Fouriert
    plt.figure()
    plt.title(plotname)
    plt.plot(x.werte[:end], y.werte[:end],color='blue', label='Schwingkreis 1')
    plt.plot(x.werte[:end], y_2.werte[:end],color='magenta', label='Schwingkreis 2')
    plt.xlabel(xstr)
    plt.legend()
    plt.ylabel(ystr)
    plt.grid()
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname + '.pdf', bbox_inches='tight')
        
'''for filename in sorted(os.listdir(cassy_dir)):
    if 'Schwebung' in filename:
        cassy_plot_clear_2(cassy_dir + filename, "t", "U_A1",cassy_dir + filename, 'U_B1',  filename[:-5], 800)'''
        
for filename in sorted(os.listdir(cassy_dir)):
    if 'Schwebung_0cm' in filename:
        cassy_plot_clear_2(cassy_dir + filename, "t", "U_A1",cassy_dir + filename, 'U_B1',  filename[:-5], -1)      