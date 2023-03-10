import pandas as pd
from praktikum import cassy, analyse
from pylab import *
import re
import os
import numpy as np
import matplotlib.ticker as ticker

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
     
    start = 660
    end = 710
     
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
        lin_U = np.log(np.abs((-1 * y.werte + U_0)/U_0))[start:end]
    else:
        lin_U = np.log(np.abs((y.werte - U_off)/U_0))[start:end]
         
    lin_I = np.log(np.abs((z_I.werte - I_off)/I_0))[start:end]
     
    return x.werte[start:end], y.werte[start:end], z_I.werte[start:end], lin_U, lin_I
 
def lin_reg(x, y, y_err, y_label, plotname=''):
    plt.rcParams['font.size'] = 28.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.linewidth'] = 0.75
    plt.rcParams['lines.linewidth'] = 0.5
    plt.rcParams['savefig.pad_inches'] = 1
    fig, axarray = plt.subplots(2, 1, figsize=(20,10), sharex=True, gridspec_kw={'height_ratios': [5, 2]})

    R,eR,b,eb,chiq,corr = analyse.lineare_regression(x, y, y_err)
    #print('Chiquadrat / nf:', chiq / (len(x)-2))
    #print('b:', b)
    axarray[0].plot(x, R*x+b, color='green')
    sigmaRes = np.sqrt((R*0)**2 + y_err**2)
    axarray[0].errorbar(x, y, yerr=y_err, color='red', fmt='.', marker='o', markeredgecolor='red')
    axarray[0].set_xlabel('$t$ / s')
    axarray[0].set_ylabel(y_label)

    axarray[1].axhline(y=0., color='black', linestyle='--')
    axarray[1].errorbar(x, y-(R*x+b), yerr=sigmaRes, color='red', fmt='.', marker='o', markeredgecolor='red', linewidth=2)
    axarray[1].set_xlabel(y_label)
    axarray[1].set_ylabel('$(U-(RI+b))$ / V')

    if SHOW_PLOTS: plt.show()
    elif plotname != '': plt.savefig("../plots/" + plotname+ '.pdf', bbox_inches = 'tight')
    return R, eR, chiq / (len(x)-2)
  
 
global start
start = 560
global end
end = 610
 
 #beispiel welches abgescheichert werden soll.
example = 'messung-aufladen-kondensator-01'

sigma_U = 0.00142
sigma_I = 4.24*10**(-6)

def sigma_lin_U(U_i, sigma_U):
    lin_U_stat = 1/((U_i-U_off))*sigma_U
    return lin_U_stat

def sigma_lin_I(I_i, sigma_I):
    lin_I_stat = 1/((I_i-I_off))*sigma_I
    return lin_I_stat

def sigma_lin_U_A(U_i, sigma_U):
    lin_U_stat_A = -1/((U_0-U_i))*sigma_U
    return lin_U_stat_A

tau_einzeln = []
tau_einzeln_stat = []
chi = []
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
            m, m_err, chi_n = lin_reg(t, lin_U, np.array(error_U), 'U / V', plotname=filename+'_linreg_U')
            tau_einzeln.append(-1/m)
            tau_einzeln_stat.append(m_err/m**2)
            chi.append(chi_n)
            m, m_err, chi_n = lin_reg(t, lin_I, np.array(error_I), 'I / A', plotname=filename+'_linreg_I')
            tau_einzeln.append(-1/m)
            tau_einzeln_stat.append(m_err/m**2)
            chi.append(chi_n)
            
def plot_tau_errorbar(y, yerr, plotname):
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.linewidth'] = 0.75
    plt.rcParams['lines.linewidth'] = 0.5
    plt.rcParams['savefig.pad_inches'] = 1
     
    fig, ax = plt.subplots()
    plt.errorbar(range(1, len(y)+1), y, yerr=yerr, fmt='.', markersize=8, capsize=2, capthick=0.8, elinewidth=1.5, label = "Tau mit Fehler")
    plt.ylabel("Tau in s")
    plt.autoscale()
    formatter = ticker.ScalarFormatter(useOffset=False)
    ax.yaxis.set_major_formatter(formatter)
    plt.title("Errorbar Plot für alle tau")
    ax.yaxis.set_label_coords(-0.2,0.50)
    plt.grid()
    plt.plot(range(1, len(y)+1), 0.01016*np.ones(16), linewidth = 1.5, label = "Mittelwert")
    plt.legend()
    plt.savefig("../plots/Errorbar_Tau_CASSY.pdf", bbox_inches='tight')
    
plot_tau_errorbar(tau_einzeln, tau_einzeln_stat, 'Errorbar Plot für alle Tau')
messdaten_tau = {'tau Spannung': tau_einzeln[::2], 'tau Spannung stat.': tau_einzeln_stat[::2], 'Chi Spannung':chi[::2], 'tau Strom': tau_einzeln[1::2], 'tau Strom stat.': tau_einzeln_stat[1::2], 'Chi Strom':chi[1::2]}
print(pd.DataFrame(messdaten_tau))
#for i in range(len(tau_einzeln)//2):
    #print('Aufladen Kondensator 01 & ' + str(round(tau_einzeln[2*i], 4)) + ' & ' + str(round(tau_einzeln_stat[2*i], 7)) + ' & ' + str(round(chi[2*i],1)) + ' \\\\')

#for i in range(len(tau_einzeln)//2):
    #print('Aufladen Kondensator 01 & ' + str(round(tau_einzeln[2*i+1], 4)) + ' & ' + str(round(tau_einzeln_stat[2*i+1], 7)) + ' & ' + str(round(chi[2*i+1],1)) + ' \\\\')

tau_einzeln = np.array(tau_einzeln)
tau_einzeln_stat = np.array(tau_einzeln_stat)
tau= sum(tau_einzeln/tau_einzeln_stat**2)/sum(1/tau_einzeln_stat**2)
tau_stat = np.sqrt(1/sum(1/tau_einzeln_stat**2))
print('tau_mean Spannung = ', np.mean(tau_einzeln[::2]))
print('tau_mean Stromstärke= ', np.mean(tau_einzeln[1::2]))
print('tau_mean = ', tau)
print('tau stat = ', tau_stat)
R = 995.5
faktor = 1000000
C = faktor * tau / R 
C_stat = faktor * 1/R * tau_stat
R_syst = 12.2
C_syst = faktor * tau / R **2 * R_syst
print(f'C = {C:.4}uF')
print(f'C syst ={C_syst:.2f} uF')
print(f'C stat ={C_stat:.4f} uF')
 
## systematischer Fehler
 
 ## generiere plot mit groesserer abweichung
end = 860
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
            lin_reg(t, lin_U, np.array(error_U), 'U / V', plotname=filename+'_linreg_U_gross')
            break
