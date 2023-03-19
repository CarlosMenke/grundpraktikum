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
         

#cassy_plot_fft(cassy_dir + "gegensinnig_01" + ".labx", "t", "U_A1", "gegensinnig_01", 3, True)
f_plus = np.array([1054, 1047, 1063.5, 1055, 1071.5, 1061.5, 1079.5, 1068, 1086.8, 1073, 1092.8, 1078.5])
f_minus = np.array([1177, 1188, 1163.5, 1176.5, 1153.5, 1167.5, 1143, 1158.5, 1133.5, 1152.5, 1121, 1146.5])

def k_calc(f1, f2):
    return (f1**2-f2**2)/(f1**2+f2**2)
k = [ k_calc(f1, f2) for f1, f2 in zip(f_minus, f_plus)]

k2 = k[::2]
k1 = k[1::2]

def sigma_k_calc(f_plus, f_minus):
    return 4*1.2*(f_plus*f_minus)/(f_plus**2+f_minus**2)**2*np.sqrt(f_minus**2+f_plus**2)

k1_err = np.array([ sigma_k_calc(f1, f2) for f1, f2 in zip(f_plus[1::2], f_minus[1::2])])
k2_err = np.array([ sigma_k_calc(f1, f2) for f1, f2 in zip(f_plus[::2], f_minus[::2])])
abstand = np.array([0, 0.5, 1, 1.5, 2, 2.5])
print("Abstand \t k1 \t k1_err")
for i in range(len(k1)):
    print(str(abstand[i]) + "cm SK1 & ", str(round(k1[i], 3)), " & " + str(round(k1_err[i], 3))+ " \\\\")
    print(str(abstand[i]) + "cm SK2 & ", str(round(k2[i], 3)), " & " + str(round(k2_err[i], 3))+ " \\\\")
 
plt.figure()
plt.title("Kopplung gegen Abstand")
plt.errorbar(abstand, k1, yerr=k1_err, color='blue', label="SK1")
plt.errorbar(abstand, k2, yerr=k2_err, color='magenta', label="SK2")
plt.xlabel("abstand in cm")
plt.ylabel("Kopplung")
plt.ylim(0, 0.13)
plt.grid()
plt.legend()
plt.savefig('../plots/' + "Kopplung_abstand" +'.pdf', bbox_inches='tight')
 
def lin_reg(x, y, x_err, y_err, plotname):
    plt.rcParams['font.size'] = 28.0
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.labelweight'] = 'normal'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['lines.linewidth'] = 2.0
    plt.rcParams["savefig.pad_inches"] = 0.5
    fig, axarray = plt.subplots(2, 1, figsize=(20,10), sharex=True, gridspec_kw={'height_ratios': [5, 2]})

    R,eR,b,eb,chiq,corr = analyse.lineare_regression_xy(x, y, x_err, y_err)
    print('Chiquadrat / nf:', chiq / (len(x)-2))
    print('b:', b)
    axarray[0].plot(x, R*x+b, color='green')
    sigmaRes = np.sqrt((R*x_err)**2 + y_err**2)
    axarray[0].errorbar(x, y, xerr=x_err, yerr=y_err, color='red', fmt='.', marker='o', markeredgecolor='red')
    axarray[0].set_xlabel('Abstand / cm')
    axarray[0].set_ylabel('Kopplung')

    axarray[1].axhline(y=0., color='black', linestyle='--')
    axarray[1].errorbar(x, y-(R*x+b), yerr=sigmaRes, color='red', fmt='.', marker='o', markeredgecolor='red', linewidth=2)
    axarray[1].set_xlabel('Abstand / cm')
    axarray[1].set_ylabel(f'$(K-({round(R, 2)}x+{round(b, 2)}))$')

    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname+ '.pdf', bbox_inches = 'tight')
    return round(R, 3), round(eR, 3), round(b, 3), round(eb, 3)


xerr = 0.001 / np.sqrt(12)
R1, eR1, b1, eb1 = lin_reg(abstand, k1, xerr * np.ones(len(abstand)), k1_err, "Kopplung_1_abstand_linreg")
R2, eR2, b2, eb2 = lin_reg(abstand, k2, xerr * np.ones(len(abstand)), k2_err, "Kopplung_2_abstand_linreg")

print("Kopplung 1: ", R1, " +- ", eR1)
print("b 1: ", b1, " +- ", eb1)
print("Kopplung 2: ", R2, " +- ", eR2)
print("b 2: ", b2, " +- ", eb2)
