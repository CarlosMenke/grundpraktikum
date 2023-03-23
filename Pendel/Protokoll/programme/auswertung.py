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
    print('b:', b)
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

    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname+ '.pdf', bbox_inches = 'tight')
    return round(R, 3), round(eR, 3), round(b, 3), round(eb, 3)


lin_reg(np.array(list(float(i) for i in list(Maxima_stange_1.keys()))), np.array(list(Maxima_stange_1.values())), 0.0001*np.ones(12), 'stange 1')
lin_reg(np.array(list(float(i) for i in list(Maxima_stange_2.keys()))), np.array(list(Maxima_stange_2.values())), 0.0001*np.ones(12), 'stange 2')
lin_reg(np.array(list(float(i) for i in list(Maxima_stange_3.keys()))), np.array(list(Maxima_stange_3.values())), 0.0001*np.ones(12), 'stange 3')
lin_reg(np.array(list(float(i) for i in list(Maxima_gewicht_1.keys()))), np.array(list(Maxima_gewicht_1.values())), 0.0001*np.ones(12), 'gewicht 1')
lin_reg(np.array(list(float(i) for i in list(Maxima_gewicht_2.keys()))), np.array(list(Maxima_gewicht_2.values())), 0.0001*np.ones(12), 'gewicht 2')
lin_reg(np.array(list(float(i) for i in list(Maxima_gewicht_3.keys()))), np.array(list(Maxima_gewicht_3.values())), 0.0001*np.ones(12), 'gewicht 3')
