#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import range

from praktikum import analyse
from praktikum import cassy
import numpy as np
import os
import matplotlib.pyplot as plt
from uncertainties import ufloat

# Gut lesbare und ausreichend große Beschriftung der Achsen, nicht zu dünne Linien:
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Arial'

# Mit Cassy aufgezeichnete Daten:
inputfile = 'labx/kondensator.labx'
#inputfile = 'txt/kondensator.txt'
data = cassy.CassyDaten(inputfile)
data.info()

# Bereich für logarithmischen Fit (in ms)
tmin = 0.101
tmax = 4.001

# Beginn der "Rauschmessung" für die Offset-Korrektur (in ms)
toffset = 8.0

plt.figure(figsize=(18,10))

N = data.anzahl_messungen()
for m in range(1, N+1):

    t = data.messung(m).datenreihe('t').werte
    data.messung(m).datenreihe('t').info()

    # Im labx-Format scheinen die Zeitwerte in s gespeichert zu sein, obwohl als Einheit "ms" angegeben ist.
    # Die Praktikumsbibliothek versucht diesen Fehler seit der Version 2.3.3 automatisch zu korrigieren,
    # gleichwohl sollte man die Zeitachse immer sorgfältig überprüfen.
    # if os.path.splitext(inputfile)[1] == '.labx':
    #     t *= 1000.0 # s -> ms, sollte ab Version 2.3.3 nicht mehr notwendig sein.

    UR = data.messung(m).datenreihe('U_A1').werte
    UC = data.messung(m).datenreihe('U_B1').werte

    plt.subplot(3,N,m)
    # Grafische Darstellung der Rohdaten
    plt.plot(t, UR, color='red', label='$U_R$')
    plt.plot(t, UC, color='green', label='$U_C$')
    plt.xlabel('$t$ / ms')
    plt.ylabel('$U$ / V')
    plt.ylim(0.,10.5)
    plt.legend(loc='right')

    plt.subplot(3,N,m+N)
    UR0 = UR[0]

    # Extrahiere Daten für Fit
    t_fit, UR_fit = analyse.untermenge_daten(t, UR, tmin, tmax)

    # Offsetkorrektur
    _, Uend = analyse.untermenge_daten(t, UR, toffset, t[-1])
    Uoffset = Uend.mean()
    print('Uoffset = %g V' % Uoffset)

    logUR_fit = np.log((UR_fit - Uoffset) / UR0)

    # Messbereich -> Digitalisierungsfehler (Cassy-ADC hat 12 bits => 4096 mögliche Werte)
    sigmaU = 20.0 / 4096. / np.sqrt(12.)
    sigmaLogUR_fit = sigmaU / UR_fit

    plt.errorbar(t_fit, logUR_fit, yerr=sigmaLogUR_fit, fmt='.')
    plt.xlabel('$t$ / ms')
    plt.ylabel('$\log\,U/U_0$')

    # Lineare Regression zur Bestimmung der Zeitkonstanten
    a,ea,b,eb,chiq,corr = analyse.lineare_regression(t_fit, logUR_fit, sigmaLogUR_fit)
    tau = -1.0 / a
    sigma_tau = abs(tau * ea/a)
    print('tau = (%s) ms   b = (%s)   chi2/dof = %g / %g' % (ufloat(tau, sigma_tau), ufloat(b, eb), chiq, len(t_fit)-2))
    plt.plot(t_fit, a*t_fit+b, color='red')

    plt.subplot(3,N,m+2*N)
    # Residuenplot
    resUR = logUR_fit - (a*t_fit+b)
    eresUR = sigmaLogUR_fit
    plt.errorbar(t_fit, resUR, yerr=eresUR, fmt='.')
    plt.xlabel('$t$ / ms')
    plt.ylabel(r'$\log\,U/U_0 - (t/\tau + b)$')

plt.tight_layout()
plt.show()
