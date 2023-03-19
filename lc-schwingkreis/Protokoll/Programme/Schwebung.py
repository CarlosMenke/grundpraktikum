import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from praktikum import analyse
from praktikum import cassy
from pylab import *
import re
import os

global SHOW_PLOTS
SHOW_PLOTS = False #for debugging, zeige alle Messdaten und die Fouriertrasformierte mit peak an.
 
global PLOTS_DIR #Ordner, in dem die Plots gespeichert werden sollen, mit passender Martrikelnummer und Versuchnummer
PLOTS_DIR = '../plots/434170_428396_1A3_'
 
cassy_dir = "../Messdaten/"

def Plot_begin_2(datei: str, x: str, y: str, datei_2: str, y_2: str):
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['lines.linewidth'] = 2.0
    plt.rcParams["savefig.pad_inches"] = 0.5

    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)

    data = cassy.CassyDaten(datei_2)
    messung = data.messung(1)
    y_2 = messung.datenreihe(y_2)
     
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
    
    return x.werte, y.werte, y_2.werte, xstr, ystr
    

# Dieser Teil des Programms Erstellt aus den Gemessenen Spannungen an Kondensator 1 und Kondensator 2 einen Plot in welchem diese gemeinsam sind
def cassy_plot_clear_2(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, start, end):
    
    x, y, y_2, xstr, ystr = Plot_begin_2(datei, x, y, datei_2, y_2)

    # Ungeschnittenen Fouriert
    plt.figure()
    plt.title(plotname)
    plt.plot(x[start:end], y[start:end],color='blue', label='Schwingkreis 1')
    plt.plot(x[start:end], y_2[start:end],color='magenta', label='Schwingkreis 2')
    plt.xlabel(xstr)
    plt.legend()
    plt.ylabel(ystr)
    plt.grid()
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname + '.pdf', bbox_inches='tight')
 
cassy_plot_clear_2('../Messdaten/Schwebung_0cm_01.labx','t', 'U_B1', '../Messdaten/Schwebung_0cm_01.labx', 'U_A1', 'Schwebung_0cm_01_Denta_T', 66, 145 )

'''for filename in sorted(os.listdir(cassy_dir)):
    if 'Schwebung' in filename and 'cm' in filename:
        cassy_plot_clear_2(cassy_dir + filename, "t", "U_B1",cassy_dir + filename, 'U_A1',  filename[:-5], 0, 500)
for filename in sorted(os.listdir(cassy_dir)):
    if 'Schwebung' in filename and 'Eisen' in filename:
        cassy_plot_clear_2(cassy_dir + filename, "t", "U_B1",cassy_dir + filename, 'U_A1',  filename[:-5], 0, 500)
'''
def cassy_plot_clear(datei: str, x: str, y: str, plotname, end, Name : str):
    # Gut lesbare und ausreichend große Beschriftung der Achsen, nicht zu dünne Linien.
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['lines.linewidth'] = 2.0
    plt.rcParams["savefig.pad_inches"] = 0.5

    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)


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

    # Ungeschnittenen Fouriert
    plt.figure()
    plt.title(plotname)
    plt.plot(x.werte[:end], y.werte[:end],color='blue', label = Name)
    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.legend()
    plt.grid()
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname + '.pdf', bbox_inches='tight')
        
'''for filename in sorted(os.listdir(cassy_dir)):
    if 'Schwebung_0cm' in filename:
        cassy_plot_clear(cassy_dir + filename, "t", "U_B1",  filename[:-5] + '_1_complete', -1, 'Schwingkreise 1') 
for filename in sorted(os.listdir(cassy_dir)):
    if 'Schwebung_0cm' in filename:
        cassy_plot_clear(cassy_dir + filename , 't',  'U_A1',  filename[:-5] + '_2_complete', -1 , 'Schwingkreis 2')
'''
cassy_plot_clear('../Messdaten/Schwebung_0cm_01.labx','t', 'U_B1', 'Schwebung_0cm_01_1_zoom', 1000, 'Schwingkreis 1') 
cassy_plot_clear('../Messdaten/Schwebung_0cm_01.labx','t', 'U_A1', 'Schwebung_0cm_01_2_zoom', 1000, 'Schwingkreis 2')       
cassy_plot_clear('../Messdaten/Schwebung_Eisenkern_01.labx', 't', 'U_B1', 'Schwebung_Eisen_01_1_complete', -1, 'Schwingkreis 1')
cassy_plot_clear('../Messdaten/Schwebung_Eisenkern_01.labx', 't', 'U_B1', 'Schwebung_Eisen_01_1_small_zoom', 2000, 'Schwingkreis 1')

def Schwebung_FFT(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, delta1, delta2):
    
    x, y, y_2, _, _ = Plot_begin_2(datei, x, y, datei_2, y_2)
    
    
    freq_fft,amp_fft = analyse.fourier_fft(x,y)
    freq_fft_2,amp_fft_2 = analyse.fourier_fft(x,y_2)
    k = min(amp_fft[535:580])
    a = np.where(amp_fft == k)[0][0]
    
    i = max(amp_fft[200:a])
    q = np.where(amp_fft == i)[0][0]
    j = max(amp_fft[a:700])
    p = np.where(amp_fft == j)[0][0]
    
    l = max(amp_fft_2[200:a])
    r = np.where(amp_fft_2 ==l)[0][0]
    m = max(amp_fft_2[a:700])
    s = np.where(amp_fft_2 == m)[0][0]

    plt.figure()
    plt.title(plotname)
    plt.plot(freq_fft[a-delta1:a+delta2],amp_fft[a-delta1:a+delta2],'.',color='blue', label = 'Schwingkreis 1')
    plt.plot(freq_fft_2[a-delta1:a+delta2],amp_fft_2[a-delta1:a+delta2],'.',color='magenta', label = 'Schwingkreis 2')
    plt.legend()
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
    
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'.pdf', bbox_inches='tight')
        
    return freq_fft[q], freq_fft[p], freq_fft_2[r], freq_fft_2[s]

f_plus_1, f_minus_1, f_plus_2, f_minus_2 = Schwebung_FFT('../Messdaten/Schwebung_0cm_01.labx', 't', 'U_B1','../Messdaten/Schwebung_0cm_01.labx' , 'U_A1', 'Schwebung_0cm_01_FFT_complete', 550, 5000) 
f_plus_1 = 1054# da per hand abgelesen und korrigiert
f_minus_1 = 1177 # da per hand abgelesen und korrigiert
f_plus_2 = 1047# da per hand abgelesen und korrigiert
f_minus_2 = 1188 # da per hand abgelesen und korrigiert
print('Fplus_1', f_plus_1)   
print('Fminus_1', f_minus_1)    
print('fplus_2', f_plus_2)
print('fminus_2', f_minus_2)
Schwebung_FFT('../Messdaten/Schwebung_0cm_01.labx', 't', 'U_B1','../Messdaten/Schwebung_0cm_01.labx' , 'U_A1', 'Schwebung_0cm_01_FFT_zoom', 100, 100) 


def f_s(f_plus, f_minus):
    f_s = (f_minus-f_plus)/2
    return f_s
def f_k(f_plus, f_minus):
    f_k = (f_minus+f_plus)/2
    return f_k
def k(f_plus, f_minus):
    k = (f_minus**2-f_plus**2)/(f_minus**2+f_plus**2)
    return k


R1 = 2.690
L1 = (9.02*10**(-3))
C1 = (2.301*10**(-6))
R2 = 2.880
L2 = 8.98*10**(-3)
C2 = 2.262*10**(-6)
def Delt_t(f, k, R, L, C):
    delt_t = 1/(2*np.pi*f)*(1/np.pi-np.arctan(k/R*np.sqrt(L/C)))
    return delt_t
print('Delta_T_1:', Delt_t(f_s(f_plus_1, f_minus_1), k(f_plus_1, f_minus_1), R1, L1, C1 ))
print('Delta_T_2:', Delt_t(f_s(f_plus_2, f_minus_2), k(f_plus_2, f_minus_2), R2, L2, C2 ))
print('k1:',k(f_plus_1, f_minus_1))
print('k2', k(f_plus_2, f_minus_2))
print('Schwebungsfrequenz SK 1:', f_s(f_plus_1, f_minus_1))  
print('Grundfrequenz SK 1', f_k(f_plus_1, f_minus_1))        

print('Schwebungsfrequenz SK 2:', f_s(f_plus_2, f_minus_2))
print('Grundfrequenz SK 2', f_k(f_plus_2, f_minus_2))

sigma_f_plus = 4 
sigma_f_minu = 3
def sigma_f(f_plus, f_minus):
    s = 4*1.2*(f_plus*f_minus)/(f_plus**2+f_minus**2)**2*np.sqrt(f_minus**2+f_plus**2)
    return s

print('fehler auf k' ,sigma_f(f_plus_1, f_minus_1))

def Schwebung_FFT_maxi(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, delta1, delta2, right=False):
    
    x, y, y_2, _, _ = Plot_begin_2(datei, x, y, datei_2, y_2)
    
    
    freq_fft,amp_fft = analyse.fourier_fft(x,y)
    
    i = max(amp_fft[200:550])
    q = np.where(amp_fft == i)[0][0]
    j = max(amp_fft[550:700])
    p = np.where(amp_fft == j)[0][0]
    if right:
        q = p
    
    plt.figure()
    plt.title(plotname)
    plt.plot(freq_fft[q-delta1:q+delta2],amp_fft[q-delta1:q+delta2],'.',color='blue', label = 'Messdaten')
    plt.axvline(freq_fft[q],color='green', label="Maximale Amplitude")
    plt.legend()
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
     
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'.pdf', bbox_inches='tight')


Schwebung_FFT_maxi('../Messdaten/Schwebung_0cm_01.labx', 't', 'U_B1','../Messdaten/Schwebung_0cm_01.labx' , 'U_A1', 'Schwebung_0cm_01_1_FFT_Maximum', 3, 3) 
Schwebung_FFT_maxi('../Messdaten/Schwebung_0cm_01.labx', 't', 'U_B1','../Messdaten/Schwebung_0cm_01.labx' , 'U_A1', 'Schwebung_0cm_01_2_FFT_Maximum', 3, 3, right=True)        
Schwebung_FFT_maxi('../Messdaten/Schwebung_0cm_01.labx', 't', 'U_A1','../Messdaten/Schwebung_0cm_01.labx' , 'U_A1', 'Schwebung_0cm_02_1_FFT_Maximum', 3, 3) 
Schwebung_FFT_maxi('../Messdaten/Schwebung_0cm_01.labx', 't', 'U_A1','../Messdaten/Schwebung_0cm_01.labx' , 'U_A1', 'Schwebung_0cm_02_2_FFT_Maximum', 3, 3, right=True)        

def sigma_k_calc(f_plus, f_minus):
    return 4*1.2*(f_plus*f_minus)/(f_plus**2+f_minus**2)**2*np.sqrt(f_minus**2+f_plus**2)

sigma_k_1 = sigma_k_calc(f_plus_1, f_minus_1)
sigma_k_2 = sigma_k_calc(f_plus_2, f_minus_2)
print('sigma_k_1: ', sigma_k_1)
print('sigma_k_2: ', sigma_k_2)

        
def Schwebung_FFT_maxi_2(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, delta1, delta2):
    
    x, y, y_2, _, _ = Plot_begin_2(datei, x, y, datei_2, y_2)
    
    
    freq_fft,amp_fft = analyse.fourier_fft(x,y)
    freq_fft_2,amp_fft_2 = analyse.fourier_fft(x,y_2)
    
    i = max(amp_fft[200:550])
    q = np.where(amp_fft == i)[0][0]
    j = max(amp_fft[550:700])
    p = np.where(amp_fft == j)[0][0]
    
    plt.figure()
    plt.title(plotname)
    plt.plot(freq_fft[q-delta1:q+delta2],amp_fft[q-delta1:q+delta2],'.',color='blue', label = 'Schwingkreis 1')
    plt.axvline(freq_fft[q],color='green', label="Maximum f_+")
    plt.plot(freq_fft_2[p-delta1:p+delta2],amp_fft[p-delta1:p+delta2],'.',color='blue')
    plt.axvline(freq_fft[p],color='olive', label="Maximum f_-")
    plt.legend()
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()

    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'.pdf', bbox_inches='tight')

Schwebung_FFT_maxi_2('../Messdaten/Schwebung_0cm_01.labx', 't', 'U_B1','../Messdaten/Schwebung_0cm_01.labx' , 'U_A1', 'Schwebung_0cm_01_FFT_zwei_Maximum', 7, 7)

from uncertainties import ufloat
from uncertainties.umath import *

 
L1 =  0.009023
L1err = L1 * 0.0025
L2 = 0.008981
L2err = L2 * 0.0025

R1 = 2.69
R2 = 2.88
Rerr = 0.007

C1 = 2.301 * 10**(-6)
C2 = 2.262 * 10**(-6)
Cerr = C1 * 0.0025
 
k1 = 0.094
k2 = 0.13
kerr = 0.0015

fs1 = f_s(f_plus_1, f_minus_1) 
fs2 = f_s(f_plus_2, f_minus_2)
fs_err = 0.72
 
L1 = ufloat(L1, L1err)
L2 = ufloat(L2, L2err)
R1 = ufloat(R1, Rerr)
R2 = ufloat(R2, Rerr)
C1 = ufloat(C1, Cerr)
C2 = ufloat(C2, Cerr)
k1 = ufloat(k1, kerr)
k2 = ufloat(k2, kerr)
fs1 = ufloat(fs1, fs_err)
fs2 = ufloat(fs2, fs_err)

#t1_stat = np.arctan(2 * np.pi / fs1 * sqrt(L1/C1) * k1 / R1)
#t2_stat = np.arctan(2 * np.pi / fs2 * sqrt(L2/C2) * k2 / R2)

def t_stat(R, L, C, k, fs, Rerr, Lerr, Cerr, Kerr, fserr):
    nenner = k**2/R**2*L/C/fs**2 + 1
     #= k**2/R**2*L/C/fs**2 + 1
    #return 2 * np.pi * np.sqrt( (1 / fs * np.sqrt(L/C) * Kerr / nenner)**2 + (k / R**2 / fs * np.sqrt(L/C) * Rerr / nenner)**2 + (k / R /fs * np.sqrt(L)/C**2 / 2 * Cerr / nenner)**2 + (k / R / fs * np.sqrt(1/(C*L)) / 2 * Lerr / nenner)**2 + (k / R / fs**2 * np.sqrt(L/C) * fserr / nenner)**2)

#t1_stat = t_stat(R1, L1, C1, k1, fs1, Rerr, L1err, Cerr, kerr, fs_err)
#t2_stat = t_stat(R2, L2, C2, k2, fs2, Rerr, L2err, Cerr, kerr, fs_err)
#print('t1_stat ', round(t1_stat, 3), ' s')
#print('t2_stat ', round(t2_stat, 3), ' s')

L1_1 = 9.05
L2_1 = 55.79
L1_2 = 8.98
L2_2 = 56.10
u = 0.025
def err_mu(L1, L2, u):
    sigma_mu = np.sqrt((1/L1)**2*(L2*u)**2+(L2/L1**2)**2*(L1*u)**2)
    return sigma_mu
sig_mu_1 = err_mu(L1_1, L2_1, u)
sig_mu_2 = err_mu(L1_2, L2_2, u)

print('fehler auf mu 1:', sig_mu_1)
print('Fehler auf mu 2:', sig_mu_2)
def Schwebung_FFT_Eisen(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, delta1, delta2):
    
    x, y, y_2, _, _ = Plot_begin_2(datei, x, y, datei_2, y_2)
    plt.rcParams['font.size'] = 16    
    
    freq_fft,amp_fft = analyse.fourier_fft(x,y)
    freq_fft_2,amp_fft_2 = analyse.fourier_fft(x,y_2)
    a =205

    plt.figure()
    plt.title(plotname)
    plt.plot(freq_fft[a-delta1:a+delta2],amp_fft[a-delta1:a+delta2],'.',color='blue', label = 'Schwingkreis 1')
    plt.plot(freq_fft_2[a-delta1:a+delta2],amp_fft_2[a-delta1:a+delta2],'.',color='magenta', label = 'Schwingkreis 2')
    plt.legend()
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
    
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'.pdf', bbox_inches='tight')
        
    return 
Schwebung_FFT_Eisen('../Messdaten/Schwebung_Eisenkern_01.labx', 't', 'U_B1','../Messdaten/Schwebung_Eisenkern_01.labx' , 'U_A1', 'Schwebung_Eisenkern_01_FFT_zoom', 200,600 )
Schwebung_FFT_Eisen('../Messdaten/Schwebung_Eisenkern_01.labx', 't', 'U_B1','../Messdaten/Schwebung_Eisenkern_01.labx' , 'U_A1', 'Schwebung_Eisenkern_01_FFT_zoom+', 40,180 )
def Schwebung_FFT_Eisen_max(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, delta1, delta2):
    
    x, y, y_2, _, _ = Plot_begin_2(datei, x, y, datei_2, y_2)
    plt.rcParams['font.size'] = 16    
    
    freq_fft,amp_fft = analyse.fourier_fft(x,y)
    freq_fft_2,amp_fft_2 = analyse.fourier_fft(x,y_2)
    a =205

    plt.figure()
    plt.title(plotname)
    plt.plot(freq_fft[a-delta1:a+delta2],amp_fft[a-delta1:a+delta2],'o',color='blue', label = 'Schwingkreis 1')
    plt.plot(freq_fft_2[a-delta1:a+delta2],amp_fft_2[a-delta1:a+delta2],'o',color='magenta', label = 'Schwingkreis 2')
    plt.legend()
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
    
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'.pdf', bbox_inches='tight')
        
    return 
Schwebung_FFT_Eisen_max('../Messdaten/Schwebung_Eisenkern_01.labx', 't', 'U_B1','../Messdaten/Schwebung_Eisenkern_01.labx' , 'U_A1', 'Schwebung_Eisenkern_01_FFT_peak',2,3)
def Schwebung_FFT_Eisen_max_2(datei: str, x: str, y: str, datei_2: str, y_2: str, plotname, delta1, delta2):
    
    x, y, y_2, _, _ = Plot_begin_2(datei, x, y, datei_2, y_2)
    plt.rcParams['font.size'] = 16   
    
    freq_fft,amp_fft = analyse.fourier_fft(x,y)
    freq_fft_2,amp_fft_2 = analyse.fourier_fft(x,y_2)
    a =353

    plt.figure()
    plt.title(plotname)
    plt.plot(freq_fft[a-delta1:a+delta2],amp_fft[a-delta1:a+delta2],'o',color='blue', label = 'Schwingkreis 1')
    plt.plot(freq_fft_2[a-delta1:a+delta2],amp_fft_2[a-delta1:a+delta2],'o',color='magenta', label = 'Schwingkreis 2')
    plt.legend()
    plt.xlabel('$f$ / Hz')
    plt.ylabel('amp')
    plt.grid()
    
    if SHOW_PLOTS:
        plt.show()
    else:
        plt.savefig('../plots/' +plotname +'.pdf', bbox_inches='tight')
        
    return 
Schwebung_FFT_Eisen_max_2('../Messdaten/Schwebung_Eisenkern_01.labx', 't', 'U_B1','../Messdaten/Schwebung_Eisenkern_01.labx' , 'U_A1', 'Schwebung_Eisenkern_01_FFT_peak_2',3,3)

f_E_plus_1 = 411
f_E_plus_2 = 410
f_E_minus_1 = 703
f_E_minus_2 = 705

k_1 = k(f_E_plus_1, f_E_minus_1)
k_2 = k(f_E_plus_2, f_E_minus_2)
print('k1 mit eisenkern', k_1)
print('k2 mit eisenkern', k_2)
sigma_k1 = sigma_k_calc(f_E_plus_1, f_E_minus_1)
sigma_k2 = sigma_k_calc(f_E_plus_2, f_E_minus_2)
print('sigma k1 eisen', sigma_k1)
print('sigma k2 eisen', sigma_k2)