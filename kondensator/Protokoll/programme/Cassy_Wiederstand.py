import matplotlib.pyplot as plt
import pandas as pd
from praktikum import cassy, analyse
from pylab import *
import re
import os
import numpy as np

global SHOW_PLOTS
SHOW_PLOTS = False #for debugging, zeige alle Messdaten und die Fouriertrasformierte mit peak an.
 
cassy_dir = "../Cassy_Messdaten/"
 
 
def cassy_plot(datei: str, x: str, y: str, y_2: str, plotname: str):
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
    ax2.legend(loc = 'center left')
    ax.legend(loc = 'center right')
    
    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname + '.pdf', bbox_inches = 'tight')
    
def cassy_hist(datei: str, x: str, y: str, y_2: str, plotname: str):
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
    y_2 = messung.datenreihe(y_2)

    plt.figure()
    plt.subplot(2,1,1)
    plt.hist(y.werte, bins = 100)
    plt.xlabel("U / V")
    plt.ylabel('Anzahl')
    plt.title(plotname)
    plt.tight_layout()
    plt.grid()
    
     
    plt.subplot(2,1,2)
    plt.hist(y_2.werte, bins = 100)
    plt.xlabel("I / A")
    plt.ylabel('Anzahl')
    plt.grid()
     
    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname + '.pdf', bbox_inches = 'tight')

     
     
plots = ['messung-aufladen-kondensator-01', 'messung-entladen-kondensator-02', 'messung-wiederstand-07']
  
 
for filename in sorted(os.listdir(cassy_dir)):
    if filename.endswith((".labx")):
        if SHOW_PLOTS: 
            if "aufladen" in filename or "entladen" in filename:
                cassy_plot(cassy_dir + filename, "t", "U_B1", "I_A1", filename)
            else:
                cassy_hist(cassy_dir + filename, "t", "U_B1", "I_A1", filename)
        for plot in plots:
            if plot in filename:
                if "aufladen" in filename or "entladen" in filename:
                    cassy_plot(cassy_dir + plot + '.labx', "t", "U_B1", "I_A1", plot)
                else: 
                    cassy_hist(cassy_dir + filename, "t", "U_B1", "I_A1", plot)

def get_messdaten(datei: str, y: str):
    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    y = messung.datenreihe(y)
    return np.array(y.werte)

# auswertung zum wiederstand.
datenpunkte = 2001
 
spannung_mean = []
spannung_std = []
stromstaerke_mean = []
stromstaerke_std = []
for filename in sorted(os.listdir(cassy_dir)):
    if filename.endswith((".labx")) and 'messung-wiederstand' in filename:
        daten = get_messdaten(cassy_dir +filename, 'U_B1')
        print(len(daten), "daten")
        spannung_mean.append(np.mean(daten))
        spannung_std.append(np.std(daten, ddof=1))
        daten = get_messdaten(cassy_dir +filename, 'I_A1')
        stromstaerke_mean.append(np.mean(daten))
        stromstaerke_std.append(np.std(daten, ddof=1))
 

spannung_mean = np.array(spannung_mean)
spannung_std = np.array(spannung_std)
spannung_mean_std = spannung_std/np.sqrt(datenpunkte)
 
stromstaerke_mean = np.array(stromstaerke_mean)
stromstaerke_std = np.array(stromstaerke_std)
stromstaerke_mean_std = stromstaerke_std/np.sqrt(datenpunkte)
 
wiederstand_messdaten = {'U': spannung_mean, 'U_unischerheit': spannung_mean_std, 'U_std': spannung_std, 'I': stromstaerke_mean, 'I_unsicherheit': stromstaerke_mean_std,'I_std': stromstaerke_std}
print(pd.DataFrame(wiederstand_messdaten))

### gesmater statistischer Fehler
digitalisierung_U_std = 20 / 2**12 / np.sqrt(12)
digitalisierung_A_std = 0.006 / 2**12 / np.sqrt(12)
spannung_stat = np.sqrt(digitalisierung_U_std**2 + spannung_mean_std**2)
stromstaerke_stat = np.sqrt(digitalisierung_A_std**2 + stromstaerke_mean_std**2)
stat = {'stat Spannung': spannung_stat, 'stat Stromstärke': stromstaerke_stat}

print('statistischer Fehler: \n', pd.DataFrame(stat))
#for i in range(len(spannung_mean)):
    #print("" + str(i + 1) + " & " + str(round(spannung_mean[i], 2)) + "V & " + str(round(spannung_mean_std[i]*1000, 1)) + "mV & " + str(round(spannung_stat[i]*1000, 1)) + "mV \\\\")
 
#for i in range(len(stromstaerke_mean)):
    #print("" + str(i + 1) + " & " + str(round(stromstaerke_mean[i]*1000, 1)) + "mA & " + str(round(stromstaerke_mean_std[i]*10**9, 0)) + "nA & " + str(round(stromstaerke_stat[i]*1000, 1)) + "mA \\\\")


def lin_reg(x, y, x_err, y_err, plotname):
    fig, axarray = plt.subplots(2, 1, figsize=(20,10), sharex=True, gridspec_kw={'height_ratios': [5, 2]})

    R,eR,b,eb,chiq,corr = analyse.lineare_regression_xy(x, y, x_err, y_err)
    print('Chiquadrat / nf:', chiq / (len(x)-2))
    print('b:', b)
    axarray[0].plot(x, R*x+b, color='green')
    sigmaRes = np.sqrt((R*x_err)**2 + y_err**2)
    axarray[0].errorbar(x, y, xerr=x_err, yerr=y_err, color='red', fmt='.', marker='o', markeredgecolor='red')
    axarray[0].set_xlabel('$I$ / A')
    axarray[0].set_ylabel('$U$ / V')

    axarray[1].axhline(y=0., color='black', linestyle='--')
    axarray[1].errorbar(x, y-(R*x+b), yerr=sigmaRes, color='red', fmt='.', marker='o', markeredgecolor='red', linewidth=2)
    axarray[1].set_xlabel('$I$ / A')
    axarray[1].set_ylabel('$(U-(RI+b))$ / V')

    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname+ '.pdf', bbox_inches = 'tight')
    return R, eR

lin_reg(stromstaerke_mean, spannung_mean, stromstaerke_stat, spannung_stat, 'lineare_regression_alle')
stromstaerke_mean = np.delete(stromstaerke_mean, 0)
spannung_mean = np.delete(spannung_mean, 0)
stromstaerke_stat = np.delete(stromstaerke_stat, 0)
spannung_stat = np.delete(spannung_stat, 0)

R, R_stat = lin_reg(stromstaerke_mean, spannung_mean, stromstaerke_stat, spannung_stat, 'lineare_regression_final')

## systematischer Fehler
u_syst = (0.01 * spannung_mean + 0.005 * 10) / np.sqrt(3)
i_syst = (0.02 * stromstaerke_mean + 0.005 * 0.003) / np.sqrt(3)

R_u_oben, _ = lin_reg(stromstaerke_mean, spannung_mean + u_syst, stromstaerke_stat, spannung_stat, 'linare_regression_u_oben')
R_u_unten, _ = lin_reg(stromstaerke_mean, spannung_mean - u_syst, stromstaerke_stat, spannung_stat, 'linare_regression_u_unten')
R_u_syst = (abs(R_u_oben-R) + abs(R_u_unten-R)) / 2
R_i_oben, _ = lin_reg(stromstaerke_mean + i_syst, spannung_mean, stromstaerke_stat, spannung_stat, 'linare_regression_i_oben')
R_i_unten, _ = lin_reg(stromstaerke_mean - i_syst, spannung_mean, stromstaerke_stat, spannung_stat, 'linare_regression_i_unten')
R_i_syst = (abs(R_i_oben-R) + abs(R_i_unten-R)) / 2
R_syst = np.sqrt(R_u_syst**2 + R_i_syst**2)
 
print('R_u_stat =', R_u_oben)
print('R_i_stat =', R_i_oben)
print('R_u_stat =', R_u_unten)
print('R_i_stat =', R_i_unten)
print('R_syst =', R_syst)
print('R_stat =', R_stat)
print('R_syst =', R_syst)
print('R =', R)
print('R error:', R_stat)
