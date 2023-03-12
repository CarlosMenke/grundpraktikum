import pandas as pd
from praktikum import cassy, analyse
from pylab import *
import re
import os
import numpy as np

global SHOW_PLOTS
SHOW_PLOTS = False #for debugging, zeige alle Messdaten und die Fouriertrasformierte mit peak an.
 
cassy_dir = "../Cassy_Messdaten/"
 
 
def cassy_plot(datei: str, x: str, y: str, z_I: str, plotname: str, offset=False):
    # Gut lesbare und ausreichend große Beschriftung der Achsen, nicht zu dünne Linien.
    plt.rcParams['font.size'] = 14.0
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.labelweight'] = 'normal'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['lines.linewidth'] = 2.0
    plt.rcParams["savefig.pad_inches"] = 0.5
    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)
    z_I = messung.datenreihe(z_I)
     
    if offset: 
        end = 490
        global I_off
        I_off = np.mean(z_I.werte[:end])
        global U_off
        U_off = np.mean(y.werte[:end])
    else: end = len(x.werte)

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
    
    fig=plt.figure()
    ax=fig.add_subplot(111, label="1")
    ax2=fig.add_subplot(111, label="2", frame_on=False)
     
    ax.plot(x.werte[:end], y.werte[:end], color="black", label = 'U')
    ax2.plot(x.werte[:end], z_I.werte[:end], color='red', label = 'I')
    ax2.yaxis.tick_right()

    if log:
        if SHOW_PLOTS: plt.show()
        else: plt.savefig("../plots/" + plotname + '.pdf', bbox_inches = 'tight')
        return
     
    fig = plt.figure()
     
    start = 500
    end = 1000
    U_off = 0.04
    U_0 = 9
    I_off = 0.00003
    I_0 = 0.01
     
    lin_U = np.log((np.abs(y.werte) - U_off)/U_0)
    lin_I = np.log((np.abs(z_I.werte) - I_off)/I_0)
    
    plt.plot(x.werte[start:end], lin_U[start:end])
    plt.figure()
    plt.plot(x.werte[start:end], lin_I[start:end])
    plt.show()
    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname + '_log_'+ '.pdf', bbox_inches = 'tight')
     
 
    
    
plots = ['messung-aufladen-kondensator-01', 'messung-entladen-kondensator-02']
log = ['messung-aufladen-kondensator-01', 'messung-entladen-kondensator-02']
global I_off
global U_off
# liste, wo nur die ersten 400 datenpunkte geplottet werden, und womit die offsetwerte global gesetzt werden
offsets_filename = 'messung-aufladen-kondensator-02'
  
 
for filename in sorted(os.listdir(cassy_dir)):
    if filename.endswith((".labx")):
        if SHOW_PLOTS: 
            if "aufladen" in filename or "entladen" in filename:
                cassy_plot(cassy_dir + filename, "t", "U_B1", "I_A1", filename)
        for plot in plots:
            if plot in filename:
                if "aufladen" in filename or "entladen" in filename:
                    cassy_plot(cassy_dir + plot + '.labx', "t", "U_B1", "I_A1", plot)


print('I_off = ', I_off)
print('U_off = ', U_off)
