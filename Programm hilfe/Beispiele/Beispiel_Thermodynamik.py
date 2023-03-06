#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from praktikum import cassy
from praktikum import analyse
import numpy as np
import scipy.constants
import matplotlib.pyplot as plt
from uncertainties import ufloat

# Gut lesbare und ausreichend große Beschriftung der Achsen, nicht zu dünne Linien:
plt.rcParams['font.size'] = 24.0
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelsize'] = 'medium'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.linewidth'] = 1.2
plt.rcParams['lines.linewidth'] = 2.0

# Rauschmessung
data1 = cassy.CassyDaten('lab/Thermo_Rauschmessung.lab')
# CASSY-Datei hat Druckwerte in der 2. Spalte, Temperatur in der 3. Spalte
p = data1.messung(1).datenreihe('p_A1').werte
T = data1.messung(1).datenreihe('T_B11').werte

plt.figure(figsize=(20,10))

plt.subplot(2,1,1)
plt.title('Histogramm der Druckwerte')
plt.hist(p,bins=100,range=(1000.,1020.),color='green')
plt.xlabel('p / mbar')
plt.xlim(1000.,1020.)

p_mean = np.mean(p)
p_stdabw = np.std(p,ddof=1)
p_err = p_stdabw/np.sqrt(len(p))

print('p_mean = %f, p_stdabw = %f, p_err = %f' % (p_mean,p_stdabw,p_err))

plt.subplot(2,1,2)
plt.title('Histogramm der Temperaturwerte')
T1 = np.min(T)-0.2
T2 = np.max(T)+0.2
plt.hist(T,bins=100,range=(T1,T2),color='blue')
plt.xlabel('T / K')
plt.xlim(T1,T2)

T_mean = np.mean(T)
T_stdabw = np.std(T,ddof=1)
T_err = T_stdabw/np.sqrt(len(T))

print('T_mean = %f, T_stdabw = %f, T_err = %f' % (T_mean,T_stdabw,T_err))

# lese Daten der Hauptmessung
data2 = cassy.CassyDaten('lab/Thermo_Hauptmessung.lab')
p = data2.messung(1).datenreihe('p_A1').werte
T = data2.messung(1).datenreihe('T_B11').werte

# Ziel: Plot log(p) vs 1/T
p0 = 1013.
logP = np.log(p/p0)
Tinv = 1.0/T

# Fehlerfortpflanzung
sigma_logP = p_stdabw/p
sigma_Tinv = T_stdabw/T**2

# Untermenge fuer lineare Regression
T2, p2 = analyse.untermenge_daten(T,p,1./0.00284,1./0.00272)
logP2 = np.log(p2/p0)
Tinv2 = 1.0/T2
sigma_logP2 = p_stdabw/p2
sigma_Tinv2 = T_stdabw/T2**2

a,ea,b,eb,chiq,corr = \
        analyse.lineare_regression_xy(Tinv2,logP2,sigma_Tinv2,sigma_logP2)
Lambda = -a*scipy.constants.R
errLambda = ea*scipy.constants.R
print('Lin.Reg.: a=%s, b=%s, chi2/ndof=%.2f/%d, corr=%f' % \
      (ufloat(a, ea), ufloat(b, eb), chiq, len(Tinv2)-2, corr))
print('Lambda = (%s) kJ/mol' % ufloat(Lambda, errLambda))

plt.tight_layout()

plt.figure(figsize=(20,10))
plt.errorbar(Tinv,logP,xerr=sigma_Tinv,yerr=sigma_logP,fmt='.')
plt.plot(Tinv2,a*Tinv2+b,'-',color='red',linewidth=3)
plt.xlabel('$T^{-1} / \mathrm{K}^{-1}$')
plt.ylabel('$\log(p/p_0)$')
plt.grid()

plt.show()


