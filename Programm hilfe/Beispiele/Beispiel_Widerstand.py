#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import range

from praktikum import analyse
from praktikum import cassy
import numpy as np
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

# Cassy-Datei, die wir analysieren wollen:
inputfile = 'labx/widerstand.labx'
#inputfile = 'txt/widerstand.txt'
data = cassy.CassyDaten(inputfile)

# Es gibt nur eine einzige Messung in der Datei.
U = data.messung(1).datenreihe('U_B1').werte
I = data.messung(1).datenreihe('I_A1').werte

# Messbereich -> Digitalisierungsfehler (Cassy-ADC hat 12 bits => 4096 mögliche Werte)
sigmaU = 20.0 / 4096. / np.sqrt(12.) * np.ones(len(U))
sigmaI = 0.2 / 4096. / np.sqrt(12.) * np.ones(len(I))

# Erstelle eine schön große Abbildung mit zwei Achsenpaaren (oben für die Messdaten samt angepasster Gerade,
# unten für den Residuenplot. Die x-Achse teilen sich beide Plots. Als Höhenverhältnis verwenden wir 5:2.
fig, axarray = plt.subplots(2, 1, figsize=(20,10), sharex=True, gridspec_kw={'height_ratios': [5, 2]})

# Grafische Darstellung der Rohdaten
axarray[0].errorbar(I, U, xerr=sigmaI, yerr=sigmaU, color='red', fmt='.', marker='o', markeredgecolor='red')
axarray[0].set_xlabel('$I$ / A')
axarray[0].set_ylabel('$U$ / V')

# Lineare Regression
R,eR,b,eb,chiq,corr = analyse.lineare_regression_xy(I, U, sigmaI, sigmaU)
print('R = (%s) Ohm,   b = (%s) V,  chi2/dof = %g / %g  corr = %g' % (ufloat(R, eR), ufloat(b, eb), chiq, len(I)-2, corr))
axarray[0].plot(I, R*I+b, color='green')

# Für den Residuenplot werden die Beiträge von Ordinate und Abszisse (gewichtet mit der Steigung) quadratisch addiert.
sigmaRes = np.sqrt((R*sigmaI)**2 + sigmaU**2)

# Zunächst plotten wir eine gestrichelte Nulllinie, dann den eigentlichen Residuenplot:
axarray[1].axhline(y=0., color='black', linestyle='--')
axarray[1].errorbar(I, U-(R*I+b), yerr=sigmaRes, color='red', fmt='.', marker='o', markeredgecolor='red')
axarray[1].set_xlabel('$I$ / A')
axarray[1].set_ylabel('$(U-(RI+b))$ / V')

# Wir sorgen dafür, dass die y-Achse beim Residuenplot symmetrisch um die Nulllinie ist:
ymax = max([abs(x) for x in axarray[1].get_ylim()])
axarray[1].set_ylim(-ymax, ymax)

# Finales Layout:
plt.tight_layout()
fig.subplots_adjust(hspace=0.0)

plt.show()
