# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 07:35:17 2023

@author: Andy
"""

import matplotlib.pyplot as plt
from praktikum import analyse
import numpy as np

global SHOW_PLOTS
SHOW_PLOTS = True #for debugging, zeige alle Messdaten und die Fouriertrasformierte mit peak an.
 

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
    print((Maxima_stange_2[1] - Maxima_stange_2[i])/ (i-1))

for i in Maxima_stange_3:
    if i == 1: continue
    #print((Maxima_stange_3[1] - Maxima_stange_3[i])/ (i-1))

for i in Maxima_gewicht_1:
    if i == 1: continue
    print((Maxima_gewicht_1[1] - Maxima_gewicht_1[i])/ (i-1))
    
for i in Maxima_gewicht_2:
    if i == 1: continue
    #print((Maxima_gewicht_2[1] - Maxima_gewicht_2[i])/ (i-1))
    
for i in Maxima_gewicht_3:
    if i == 1: continue
    #print((Maxima_gewicht_3[1] - Maxima_gewicht_3[i])/ (i-1))
    
for i1, i2, i3, i4, i5, i6 in zip(Maxima_stange_1, Maxima_stange_2, Maxima_stange_3, Maxima_gewicht_1, Maxima_gewicht_2, Maxima_gewicht_3):
    print(str(i1) + " & " + str(Maxima_stange_1[i1]) + "s & ", str(i2) + " & " + str(Maxima_stange_2[i2]) + "s & ", str(i3) + " & " + str(Maxima_stange_3[i3]) + "s \\\\")

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
    print('Chiquadrat / nf:', chiq / (len(x)-2))
    print('T:', R)
    axarray[0].plot(x, R*x+b, color='green')
    sigmaRes = np.sqrt(y_err**2)
    axarray[0].errorbar(x, y, yerr=y_err, color='red', fmt='.', marker='o', markeredgecolor='red')
    axarray[0].set_xlabel('Abstand / cm')
    axarray[0].set_ylabel('Kopplung')

    axarray[1].axhline(y=0., color='black', linestyle='--')
    axarray[1].errorbar(x, y-(R*x+b), yerr=sigmaRes, color='red', fmt='.', marker='o', markeredgecolor='red', linewidth=2)
    axarray[1].set_xlabel('Abstand / cm')
    axarray[1].set_ylabel(f'$(K-({round(R, 2)}x+{round(b, 2)}))$')
    plt.title(plotname)

    #if SHOW_PLOTS: plt.show()
    #else: plt.savefig("../plots/" + plotname+ '.pdf', bbox_inches = 'tight')
    return round(R, 6), round(eR, 6), round(b, 6), round(eb, 6)


stange_T1, stange_eT1, stange_b1, stange_eb1 = lin_reg(np.array(list(float(i) for i in list(Maxima_stange_1.keys()))), np.array(list(Maxima_stange_1.values())), stange_1_err*np.ones(12), 'stange 1')
stange_T2, stange_eT2, stange_b2, stange_eb2 = lin_reg(np.array(list(float(i) for i in list(Maxima_stange_2.keys()))), np.array(list(Maxima_stange_2.values())), stange_2_err*np.ones(12), 'stange 2')
stange_T3, stange_eT3, stange_b3, stange_eb3 = lin_reg(np.array(list(float(i) for i in list(Maxima_stange_3.keys()))), np.array(list(Maxima_stange_3.values())), stange_3_err*np.ones(12), 'stange 3')
gewicht_T1, gewicht_eT1, gewicht_b1, gewicht_eb1 = lin_reg(np.array(list(float(i) for i in list(Maxima_gewicht_1.keys()))), np.array(list(Maxima_gewicht_1.values())), gewicht_1_err*np.ones(12), 'gewicht 1')
gewicht_T2, gewicht_eT2, gewicht_b2, gewicht_eb2 = lin_reg(np.array(list(float(i) for i in list(Maxima_gewicht_2.keys()))), np.array(list(Maxima_gewicht_2.values())), gewicht_2_err*np.ones(12), 'gewicht 2')
gewicht_T3, gewicht_eT3, gewicht_b3, gewicht_eb3 = lin_reg(np.array(list(float(i) for i in list(Maxima_gewicht_3.keys()))), np.array(list(Maxima_gewicht_3.values())), gewicht_3_err*np.ones(12), 'gewicht 3')
 
stange_T = np.array([stange_T1, stange_T2, stange_T3])
gewicht_T = np.array([gewicht_T1, gewicht_T2, gewicht_T3])
print('T stange', stange_T)
print('T gewicht', gewicht_T)
error_T_relativ = np.mean(stange_T) / np.mean(gewicht_T)
print('T error von stange zu gewicht', error_T_relativ)
