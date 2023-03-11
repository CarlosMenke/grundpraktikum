import matplotlib.pyplot as plt
from praktikum import analyse
from praktikum import cassy
from pylab import *
import re
import os

global SHOW_PLOTS
SHOW_PLOTS = False #for debugging, zeige alle Messdaten und die Fouriertrasformierte mit peak an.
 
cassy_dir = "../Cassy_Messdaten/"
 
 
def cassy_plot(datei: str, x: str, y: str, y_2: str, plotname: str):
    # Gut lesbare und ausreichend große Beschriftung der Achsen, nicht zu dünne Linien.
    plt.rcParams['font.size'] = 14.0
    plt.rcParams['font.family'] = 'sans-serif'
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

    fig=plt.figure()
    #axi =  plt.subplot()
    ax=fig.add_subplot(111, label="1")
    ax2=fig.add_subplot(111, label="2", frame_on=False)
    
    ax.plot(x.werte, y.werte, color="black", label = 'U')
    ax2.plot(x.werte, y_2.werte, color='red', label = 'I')
    ax2.yaxis.tick_right()

    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.title(plotname)
    ax2.yaxis.set_label_coords(-0.2, 0.5)
    ax.set_ylabel('I_A1/ A')
    ax.yaxis.set_label_position('right') 
    ax.yaxis.set_label_coords(1.2, 0.5)
    ax2.legend(loc = 'upper left')
    ax.legend(loc = 'upper right')
    
    #ax2-plt.ylabel(y_2str)
    
    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname, bbox_inches = 'tight')
    
plots = ['messung-aufladen-kondensator-01']
  
 
for filename in sorted(os.listdir(cassy_dir)):
    if filename.endswith((".labx")):
        if SHOW_PLOTS: cassy_plot(cassy_dir + filename, "t", "U_B1", "I_A1", plot)
        for plot in plots:
            if plot in filename:
                cassy_plot(cassy_dir + plot + '.labx', "t", "U_B1", "I_A1", plot)
