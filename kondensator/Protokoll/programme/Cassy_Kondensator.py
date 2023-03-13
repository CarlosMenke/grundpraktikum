import pandas as pd
from praktikum import cassy, analyse
from pylab import *
import re
import os
import numpy as np

global SHOW_PLOTS
SHOW_PLOTS = False #for debugging, zeige alle Messdaten und die Fouriertrasformierte mit peak an.
 
cassy_dir = "../Cassy_Messdaten/"
 
 
def cassy_plot(datei: str, x: str, y: str, z_I: str, plotname: str, log=False, offset=False, offset_u0=False):
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
    z_I = messung.datenreihe(z_I)
     
    if offset_u0:
        end = 490
        global U_0
        global I_0
        U_0 = np.mean(y.werte[:end])
        global U_0_fehler
        U_0_fehler = np.std(y.werte[:end]) / np.sqrt(end)
         
        I_0 = min(z_I.werte[490:550])
    elif offset:
        end = 490
        global I_off
        I_off = np.mean(z_I.werte[:end])
        global U_off
        U_off = np.mean(y.werte[:end])
        global U_fehler
        U_fehler = np.std(y.werte[:end]) / np.sqrt(end)
    else: end = len(x.werte)

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
    ax=fig.add_subplot(111, label="1")
    ax2=fig.add_subplot(111, label="2", frame_on=False)
     
    ax.plot(x.werte[:end], y.werte[:end], color="black", label = 'U')
    ax2.plot(x.werte[:end], z_I.werte[:end], color='red', label = 'I')
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

    if not log:
        if SHOW_PLOTS: plt.show()
        else: plt.savefig("../plots/" + plotname + '.pdf', bbox_inches = 'tight')
        return
     
    fig = plt.figure()
     
    start = 510
    end = 1010
     
    plt.figure()
    if 'aufladen' in datei:
        lin_U = np.log(np.abs((-1 * y.werte + U_0)/U_0))
        plt.ylabel('log((- |U_B1| + U_0)/U_0)')
    else:
        lin_U = np.log(np.abs((y.werte - U_off)/U_0))
        plt.ylabel('log((|U_B1| 0 U_off)/U_0)')
         
    plt.plot(x.werte[start:end], lin_U[start:end])
    plt.xlabel(xstr)
    plt.title(plotname + 'Spannung')
    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname + '_U_log'+ '.pdf', bbox_inches = 'tight')
     
    lin_I = np.log(np.abs((z_I.werte - I_off)/I_0))
    plt.figure()
    plt.title(plotname + 'Stromstärke')
    plt.plot(x.werte[start:end], lin_I[start:end])
    plt.xlabel(xstr)
    plt.ylabel('log((|I_A1| 0 I_off)/I_0)')
    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname + '_A_log' + '.pdf', bbox_inches = 'tight')
     
    if plotname in show_complete:
        start = 500
        end = len(x.werte)
    else: return

     
    plt.figure()
    if 'aufladen' in datei:
        lin_U = np.log(np.abs((-1 * y.werte + U_0)/U_0))
        plt.ylabel('log((- |U_B1| + U_0)/U_0)')
    else:
        lin_U = np.log(np.abs((y.werte - U_off)/U_0))
        plt.ylabel('log((|U_B1| 0 U_off)/U_0)')
         
    plt.plot(x.werte[start:end], lin_U[start:end])
    plt.xlabel(xstr)
    plt.title(plotname + ' Spannung')
    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname + '_U_log_complete'+ '.pdf', bbox_inches = 'tight')
     
    lin_I = np.log(np.abs((z_I.werte - I_off)/I_0))
    plt.figure()
    plt.title(plotname + ' Stromstärke')
    plt.plot(x.werte[start:end], lin_I[start:end])
    plt.xlabel(xstr)
    plt.ylabel('log((|I_A1| 0 I_off)/I_0)')
    if SHOW_PLOTS: plt.show()
    else: plt.savefig("../plots/" + plotname + '_A_log_complete' + '.pdf', bbox_inches = 'tight')
    
    
 
    
    
global I_off
global U_off
global U_fehler
global U_0
global U_0_fehler
global I_0
# liste, wo nur die ersten 400 datenpunkte geplottet werden, und womit die offsetwerte global gesetzt werden
global offsets_filename
cassy_plot(cassy_dir +  'messung-aufladen-kondensator-02' + '.labx', "t", "U_B1", "I_A1", "messung-offset", offset=True)
cassy_plot(cassy_dir +  'messung-entladen-kondensator-02' + '.labx', "t", "U_B1", "I_A1", "messung-offset_u0", offset_u0=True)
plots = ['messung-aufladen-kondensator-01', 'messung-entladen-kondensator-02']
plots_log = ['aufladen-kondensator-01', 'aufladen-kondensator-01', 'entladen-kondensator-02']
global show_complete
show_complete = ['aufladen-kondensator-01']
  
 
for filename in sorted(os.listdir(cassy_dir)):
    if filename.endswith((".labx")):
        if SHOW_PLOTS: 
            if "aufladen" in filename or "entladen" in filename:
                cassy_plot(cassy_dir + filename, "t", "U_B1", "I_A1", filename)
                cassy_plot(cassy_dir + filename + '.labx', "t", "U_B1", "I_A1", '...', log=True)
        else:
            for plot in plots:
                if plot in filename:
                    if "aufladen" in filename or "entladen" in filename:
                        cassy_plot(cassy_dir + filename, "t", "U_B1", "I_A1", plot)
                        pass
            for plot in plots_log:
                if plot in filename:
                    cassy_plot(cassy_dir + filename, "t", "U_B1", "I_A1", plot, log=True)


print('I_off = ', I_off)
print('I_0 = ', I_0)
print('U_off = ', U_off)
print('U_0 = ', U_0)
 
def get_log_values(datei, x, y, z_I):
    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)
    z_I = messung.datenreihe(z_I)

    if 'aufladen' in datei:
        lin_U = np.log(np.abs((-1 * y.werte + U_0)))[start:end]
    else:
        lin_U = np.log(np.abs((y.werte - U_off)))[start:end]
         
    lin_I = np.log(np.abs((z_I.werte - I_off)))[start:end]
     
    return x.werte[start:end], y.werte[start:end], z_I.werte[start:end], lin_U, lin_I
 
def lin_reg(x, y, y_err, plotname=''):
    fig, axarray = plt.subplots(2, 1, figsize=(20,10), sharex=True, gridspec_kw={'height_ratios': [5, 2]})

    R,eR,b,eb,chiq,corr = analyse.lineare_regression(x, y, y_err)
    print('Chiquadrat / nf:', chiq / (len(x)-2))
    print('b:', b)
    axarray[0].plot(x, R*x+b, color='green')
    sigmaRes = np.sqrt((R*0)**2 + y_err**2)
    axarray[0].errorbar(x, y, yerr=y_err, color='red', fmt='.', marker='o', markeredgecolor='red')
    axarray[0].set_xlabel('$I$ / A')
    axarray[0].set_ylabel('$U$ / V')

    axarray[1].axhline(y=0., color='black', linestyle='--')
    axarray[1].errorbar(x, y-(R*x+b), yerr=sigmaRes, color='red', fmt='.', marker='o', markeredgecolor='red', linewidth=2)
    axarray[1].set_xlabel('$I$ / A')
    axarray[1].set_ylabel('$(U-(RI+b))$ / V')

    if SHOW_PLOTS: plt.show()
    elif plotname != '': plt.savefig("../plots/" + plotname+ '.pdf', bbox_inches = 'tight')
    return R, eR
  
 
global start
start = 610
global end
end = 660
t_err = 50 * 10**(-6) / np.sqrt(12) * np.ones(end-start)
t_err = 10**(-10) * np.ones(end-start)
 
 #beispiel welches abgescheichert werden soll.
example = 'messung-aufladen-kondensator-01'

sigma_U = 0.00142
sigma_I = 1.44*10**(-6)

def sigma_lin_U(U_i, sigma_U):
    lin_U_stat = 1/((U_i-U_off))*sigma_U
    return lin_U_stat

def sigma_lin_I(I_i, sigma_I):
    lin_I_stat = 1/((I_i+I_off))*sigma_I
    return lin_I_stat

def sigma_lin_U_A(U_i, sigma_U):
    lin_U_stat_A = -1/((U_0-U_i))*sigma_U
    return lin_U_stat_A

tau_einzeln = []
tau_einzeln_stat = []
for filename in sorted(os.listdir(cassy_dir)):
    if filename.endswith((".labx")):
        if '03' in filename: continue
        if "messung-aufladen" in filename or "messung-entladen" in filename:
            t, y, z_I, lin_U, lin_I = get_log_values(cassy_dir + filename, "t", "U_B1", "I_A1")
            error_U = []
            if 'aufladen' in filename:
                for i in y : 
                    u = sigma_lin_U_A(i, sigma_U) 
                    error_U.append(abs(u))
            else:
                for i in y:
                    u = sigma_lin_U(i, sigma_U)
                    error_U.append(u)
            error_I = []
            for j in z_I:
                i = sigma_lin_I(j, sigma_I)
                error_I.append(abs(i))
            m, m_err = lin_reg(t, lin_U, np.array(error_U), plotname=filename+'_linreg_U')
            tau_einzeln.append(-1/m)
            tau_einzeln_stat.append(-1/m_err)
            m, m_err = lin_reg(t, lin_I, np.array(error_I), plotname=filename+'_linreg_I')
            tau_einzeln.append(-1/m)
            tau_einzeln_stat.append(-1/m_err)
print('tau_einzeln = ', tau_einzeln)
