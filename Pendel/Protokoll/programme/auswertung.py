# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 07:35:17 2023

@author: Andy
"""

import matplotlib.pyplot as plt
from praktikum import analyse
import numpy as np
import pandas as pd

global SHOW_PLOTS
SHOW_PLOTS = False #for debugging, zeige alle Messdaten und die Fouriertrasformierte mit peak an.
 

# anzahl maximum: zeit
Maxima_stange_1 = {2:3.138, 11:18.063, 20:32.935, 30:49.473, 40:66.058, 50:82.598, 60:99.190, 70:115.729, 79:130.651, 90:148.843, 101:167.079, 112:185.279}
Maxima_stange_2 = {1:1.455, 10:16.382, 20:32.944, 29:47.857, 39:64.411, 50:82.628, 60:99.192, 69:114.075, 80:132.288, 90:148.857, 100:165.417, 111:183.626}
Maxima_stange_3 = {1:1.528, 11:18.088, 20:33.022, 29:47.909, 39:64.471, 51:84.347, 60:99.269, 69:114.162, 79:130.7, 90:148.936, 101:167.164, 111:183.715}
 
Maxima_gewicht_1 = {1:1.508, 11:18.062, 21:34.581, 31:51.141, 41:67.679, 50:82.562, 60:99.13, 70:115.653, 79:130.521, 91:150.368, 99:163.627, 108:178.526}
Maxima_gewicht_1_test = {2:3.296, 10:16.556, 21:34.729, 31:51.253, 41:67.831, 50:82.704, 60:99.246, 70:115.769, 79:130.676, 90:148.864, 100:165.389, 111:183.599}
Maxima_gewicht_2 = {1:1.636, 11:18.176, 21:34.733, 31:51.253, 39:64.501, 50:82.710, 60:99.246, 69:114.136, 82:135.616, 91:150.532, 100:165.394, 111:183.606}
Maxima_gewicht_3 = {1:1.59, 12:19.772, 21:34.653, 30:49.539, 39:64.445, 50:82.636, 59:97.518, 69:114.06, 80:132.239, 90:148.788, 101:166.969, 110:181.893}


for i in Maxima_stange_1:
    if i == 2: continue
    #print((Maxima_stange_1[2] - Maxima_stange_1[i])/ (i-2))

for i in Maxima_stange_2:
    if i == 1: continue
    #print((Maxima_stange_2[1] - Maxima_stange_2[i])/ (i-1))

for i in Maxima_stange_3:
    if i == 1: continue
    #print((Maxima_stange_3[1] - Maxima_stange_3[i])/ (i-1))

for i in Maxima_gewicht_1:
    if i == 1: continue
    #print((Maxima_gewicht_1[1] - Maxima_gewicht_1[i])/ (i-1))
    
for i in Maxima_gewicht_2:
    if i == 1: continue
    #print((Maxima_gewicht_2[1] - Maxima_gewicht_2[i])/ (i-1))
    
for i in Maxima_gewicht_3:
    if i == 1: continue
    #print((Maxima_gewicht_3[1] - Maxima_gewicht_3[i])/ (i-1))
    
# damit wir nicht alles von hand in latex tippen müssen
for i1, i2, i3, i4, i5, i6 in zip(Maxima_stange_1, Maxima_stange_2, Maxima_stange_3, Maxima_gewicht_1, Maxima_gewicht_2, Maxima_gewicht_3):
    #print(str(i1) + " & " + str(Maxima_stange_1[i1]) + "s & ", str(i2) + " & " + str(Maxima_stange_2[i2]) + "s & ", str(i3) + " & " + str(Maxima_stange_3[i3]) + "s \\\\")
    pass
for i1, i2, i3, i4, i5, i6 in zip(Maxima_stange_1, Maxima_stange_2, Maxima_stange_3, Maxima_gewicht_1, Maxima_gewicht_2, Maxima_gewicht_3):
    #print(str(i4) + " & " + str(Maxima_gewicht_1[i4]) + "s & ", str(i5) + " & " + str(Maxima_gewicht_2[i5]) + "s & ", str(i6) + " & " + str(Maxima_gewicht_3[i6]) + "s \\\\")
    pass

def maximale_abweichung(l):
    return max(abs(min(l) - np.mean(np.array(l))), abs(max(l) - np.mean(np.array(l))))

error_stange_1 = []


error_stange_1 = [3.141, 3.134, 3.142, 3.137, 3.142, 3.133]
error_stange_1 = [8.105, 8.099, 8.10, 8.088, 8.098, 8.107]
stange_1_err = maximale_abweichung(error_stange_1)
print(stange_1_err)
error_stange_2 = [3.14, 3.144, 3.150, 3.141, 3.139, 3.143]
stange_2_err = maximale_abweichung(error_stange_2)
error_stange_3 = [3.197, 3.204, 3.187, 3.194, 3.201, 3.202, 3.201]
stange_3_err = maximale_abweichung(error_stange_3)

error_gewicht_1 = [4.816, 4.806, 4.816, 4.812, 4.824, 4.819]
gewicht_1_err = maximale_abweichung(error_gewicht_1)
error_gewicht_2 = [3.296, 3.286, 3.293, 3.295, 3.2923, 3.304]
gewicht_2_err = maximale_abweichung(error_gewicht_2)
error_gewicht_3 = [9.852, 9.841, 9.843, 9.845, 9.855, 9.840, 9.85]
gewicht_3_err = maximale_abweichung(error_gewicht_3)
print(gewicht_1_err)
errors = [stange_1_err, stange_2_err, stange_3_err, gewicht_1_err, gewicht_2_err, gewicht_3_err]
print(pd.DataFrame(errors, ['stat Fehler Stange1', 'stat Fehler Stange2', 'stat Fehler Stange3', 'stat Fehler Gewicht1', 'stat Fehler Gewicht2', 'stat Fehler Gewicht3']).round(4))

def lin_reg(x, y, y_err, plotname):
    plt.rcParams['font.size'] = 28.0
    plt.rcParams['font.weight'] = 'normal'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.labelweight'] = 'normal'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['lines.linewidth'] = 2.0
    plt.rcParams["savefig.pad_inches"] = 0.5
    fig, axarray = plt.subplots(2, 1, figsize=(20,10), sharex=True, gridspec_kw={'height_ratios': [5, 2]})

    R,eR,b,eb,chiq,corr = analyse.lineare_regression(x, y, y_err)
    print('Chiquadrat / nf:', round(chiq / (len(x)-2), 1))
    print('T:', round(R, 4))
    axarray[0].plot(x, R*x+b, color='green')
    sigmaRes = np.sqrt(y_err**2)
    axarray[0].grid()
    axarray[1].grid()
    axarray[0].errorbar(x, y, yerr=y_err, color='red', fmt='.', marker='o', markeredgecolor='red')
    axarray[0].set_xlabel('Anzahl')
    axarray[0].set_ylabel('Zeit / s')

    axarray[1].axhline(y=0., color='black', linestyle='--')
    axarray[1].errorbar(x, y-(R*x+b), yerr=sigmaRes, color='red', fmt='.', marker='o', markeredgecolor='red', linewidth=2)
    axarray[1].set_xlabel('Anzahl')
    axarray[1].set_ylabel(f'$(T-({round(R, 4)}s*N+{round(b, 4)}s))$')

    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + 'lineare_regression_' + plotname+ '.pdf', bbox_inches = 'tight')
    return R, eR, b, eb


stange_T1, stange_eT1, stange_b1, stange_eb1 = lin_reg(np.array(list(float(i) for i in list(Maxima_stange_1.keys()))), np.array(list(Maxima_stange_1.values())), stange_1_err*np.ones(12), 'stange_1')
stange_T2, stange_eT2, stange_b2, stange_eb2 = lin_reg(np.array(list(float(i) for i in list(Maxima_stange_2.keys()))), np.array(list(Maxima_stange_2.values())), stange_2_err*np.ones(12), 'stange_2')
stange_T3, stange_eT3, stange_b3, stange_eb3 = lin_reg(np.array(list(float(i) for i in list(Maxima_stange_3.keys()))), np.array(list(Maxima_stange_3.values())), stange_3_err*np.ones(12), 'stange_3')
gewicht_T1, gewicht_eT1, gewicht_b1, gewicht_eb1 = lin_reg(np.array(list(float(i) for i in list(Maxima_gewicht_1.keys()))), np.array(list(Maxima_gewicht_1.values())), gewicht_1_err*np.ones(12), 'gewicht_1')
gewicht_T2, gewicht_eT2, gewicht_b2, gewicht_eb2 = lin_reg(np.array(list(float(i) for i in list(Maxima_gewicht_2.keys()))), np.array(list(Maxima_gewicht_2.values())), gewicht_2_err*np.ones(12), 'gewicht_2')
gewicht_T3, gewicht_eT3, gewicht_b3, gewicht_eb3 = lin_reg(np.array(list(float(i) for i in list(Maxima_gewicht_3.keys()))), np.array(list(Maxima_gewicht_3.values())), gewicht_3_err*np.ones(12), 'gewicht_3')
 
lin_reg_ergebnisse = pd.DataFrame([[stange_T1, stange_eT1, stange_b1, stange_eb1], [stange_T2, stange_eT2, stange_b2, stange_eb2], [stange_T3, stange_eT3, stange_b3, stange_eb3], [gewicht_T1, gewicht_eT1, gewicht_b1, gewicht_eb1], [gewicht_T2, gewicht_eT2, gewicht_b2, gewicht_eb2], [gewicht_T3, gewicht_eT3, gewicht_b3, gewicht_eb3]], columns=['T', 'eT', 'b', 'eb'], index=['stange_1', 'stange_2', 'stange_3', 'gewicht_1', 'gewicht_2', 'gewicht_3'])
print(pd.DataFrame(lin_reg_ergebnisse).round(4))

T_stange_einzeln = np.array([stange_T1, stange_T2, stange_T3])
T_stange_einzeln_stat = np.array([stange_eT1, stange_eT2, stange_eT3])
T_gewicht_einzeln = np.array([gewicht_T1, gewicht_T2, gewicht_T3])
T_gewicht_einzeln_stat = np.array([gewicht_eT1, gewicht_eT2, gewicht_eT3])
  
T_stange = sum(T_stange_einzeln / T_stange_einzeln_stat**2) / sum(1 / T_stange_einzeln_stat**2)
T_gewicht = sum(T_gewicht_einzeln / T_gewicht_einzeln_stat**2) / sum(1 / T_gewicht_einzeln_stat**2)
T_stange_stat = np.sqrt(1/sum(1/T_stange_einzeln_stat**2))
T_gewicht_stat = np.sqrt(1/sum(1/T_gewicht_einzeln_stat**2))
print('T stange', round(T_stange, 5), '+-', round(T_stange_stat, 5))
print('T gewicht', round(T_gewicht, 5), '+-', round(T_gewicht_stat, 5))
error_T_relativ = T_stange / T_gewicht
print('T error von stange zu gewicht', error_T_relativ)


l_1 = [2.595, 2.590, 2.585, 2.600, 2.605, 2.605]
l_2 = [1.110, 1.110, 1.110]
l_3 = [64.1, 64.2, 64.2]
d = [8.080, 8.080, 8.080]

l1 = np.array(l_1)
l2 = np.array(l_2)
l3 = np.array(l_3)

l1_m = np.mean(l1)
l2_m = np.mean(l2)
l3_m = np.mean(l3)


l1_sigma = np.std(l1, ddof=1)
l3_sigma = np.std(l3, ddof=1)
print('mittelwert, l1:',round(l1_m, 5))
print('sigma l1:', round(l1_sigma/np.sqrt(6), 5))


print('mean l3:',round(l3_m, 5))
print('sigma l3:', round(l3_sigma/np.sqrt(3), 5))

l = (l1_m + l2_m + l3_m)/100

g = 4 * (np.pi)**2 /(T_gewicht**2) * l * (1 + 1/2 * (d[0]/2/100)**2/(l**2))
print('g:', g)

d = d[0]/100
T = T_gewicht
#TODO check l_sigma
l_sigma = 0.029
g_stat = (8*(np.pi)**2/T**3 * l * (1 + 1/2 * d**2/(l**2)))**2 * T_gewicht_stat**2 + ()**2 * l_sigma**2
