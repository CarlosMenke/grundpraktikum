import numpy as np
from praktikum import cassy
import numpy as np
from numpy import sqrt,sin,cos,log,exp
import scipy.fft
import scipy.odr
import argparse
import matplotlib.pyplot as plt
import re

Aluminium = [12.05, 12.05, 12.06, 12.05, 12.06, 12.06, 12.06, 12.05, 12.06, 12.07]
Messing = [11.98, 12.01, 11.98, 11.99, 11.98, 11.98, 11.99, 11.99, 11.98, 11.98]
Kupfer = [11.98, 11.98, 11.98, 11.98, 11.98, 11.99, 11.98, 11.98, 11.98, 11.98]
Stahl15 = [12.00, 12.00, 11.99, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.01]
print(len(Stahl15))

Alu_NP = np.array(Aluminium)/100
M_NP = np.array(Messing)/100
K_NP = np.array(Kupfer)/100
S_NP = np.array(Stahl15)/100
#print(Alu_NP[0])
#print(len(Alu_NP))

Alu_mean = np.mean(Alu_NP)
Alu_stdabw = np.std(Alu_NP,ddof=1)
Alu_err = Alu_stdabw/np.sqrt(len(Alu_NP))

M_mean = np.mean(M_NP)
M_stdabw = np.std(M_NP,ddof=1)
M_err = M_stdabw/np.sqrt(len(M_NP))

K_mean = np.mean(K_NP)
K_stdabw = np.std(K_NP,ddof=1)
K_err = K_stdabw/np.sqrt(len(K_NP))

S_mean = np.mean(S_NP)
S_stdabw = np.std(S_NP,ddof=1)
S_err = S_stdabw/np.sqrt(len(S_NP))


print('Ergebnis: Aluminium_mean=%f+-%f' % (Alu_mean,Alu_err),'m')
print('Ergebnis: Messing_mean=%f+-%f' % (M_mean,M_err),'m')
print('Ergebnis: Kupfer_mean=%f+-%f' % (K_mean,K_err),'m')
print('Ergebnis: Stahl_mean=%f+-%f' % (S_mean,S_err),'m')
print(Alu_mean, 'Mittelwet des Durchmessers von Alu')
print(Alu_stdabw, 'Standardabweichung des Durchmessers von Alu')
print((Alu_err, 'Fehler auf den Durchmesser der Aluminiumstange'))
