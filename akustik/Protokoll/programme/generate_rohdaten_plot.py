#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from praktikum import cassy
import re

global plot_dir
plot_dir = "./"

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

    plt.figure(figsize=(20,10))
    plt.errorbar(x.werte, y.werte)

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

    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.tight_layout()
    #plt.show()
    return plt
 
cassy_dir = "../../Messungen/"
plots = [ "Roth_Menke_Alu_Messung_01", "Roth_Menke_Kupfer_Messung_02", "Roth_Menke_Stahl_Messung_01", "Roth_Menke_Messing_Messung_01" ]
for plot in plots:
    cassy_plot(cassy_dir + plot + ".labx", "t", "U_A1").savefig( plot + ".png")
