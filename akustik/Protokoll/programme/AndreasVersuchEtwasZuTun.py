import numpy as np
import pandas as pd
import os
from praktikum import cassy, analyse
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

### Durchmesser der Stangen
Aluminium = [12.05, 12.05, 12.06, 12.05, 12.06, 12.06, 12.06, 12.05, 12.06, 12.07]
Messing = [11.98, 12.01, 11.98, 11.99, 11.98, 11.98, 11.99, 11.99, 11.98, 11.98]
Kupfer = [11.98, 11.98, 11.98, 11.98, 11.98, 11.99, 11.98, 11.98, 11.98, 11.98]
Stahl15 = [12.00, 12.00, 11.99, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.01]
print(len(Stahl15))

Alu_NP = np.array(Aluminium)/1000
M_NP = np.array(Messing)/1000
K_NP = np.array(Kupfer)/1000
S_NP = np.array(Stahl15)/1000
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


#Berechnung des Mittelwerts der dichte
De =[Alu_err, M_err, K_err, S_err]
D = [Alu_mean, M_mean, K_mean, S_mean]
M = [0.4609, 1.4275, 1.5054, 1.3274]
L = 1.5

def roh(D, M, L):
    print(D,M,L)
    roh = M/(np.pi*(D/2)**2*L)
    return roh

for i, j in zip(D, M):
    p = roh(i, j, L)
    if i == Alu_mean:
        print("Dichte von Aluminium:", f"{p:.2f}" )
    if i == M_mean:
        print("Dichte von Messing", f"{p:.2f}")
    if i == K_mean:
        print("Dichte von Kupfer", f"{p:.2f}")   
    if i == S_mean:
        print("Dichte von Stahl15", f"{p:.2f}")    
 # Fehlerfortplanzung des Statistischen Fehlers auf die Dichte 
       
def sigma_roh(D, M, L, De):
    s = ((8*M)/(np.pi*D**3*L))**2*De**2
    return s

for i, j, k in zip(D, M, De):
    roh_err = np.sqrt(sigma_roh(i, j, L, k))
    if i == Alu_mean:
        print("stat. Fehler auf Dichte von Aluminium:", f"{roh_err:.2f}" )
    if i == M_mean:
        print("stat. Fehler auf Dichte von Messing", f"{roh_err:.2f}")
    if i == K_mean:
        print("stat. Fehler auf Dichte von Kupfer", f"{roh_err:.2f}")   
    if i == S_mean:
        print("stat. Fehler auf Dichte von Stahl15", f"{roh_err:.2f}")    
    
   
def fft_peak(datei: str, x: str, y: str, plotname: str, save_peak: bool = True):
    start = start_values[plotname] if plotname in start_values else 0
     
    data = cassy.CassyDaten(datei)
    messung = data.messung(1)
    x = messung.datenreihe(x)
    y = messung.datenreihe(y)
     
     # Fourier-Transformation
    freq_fft,amp_fft = analyse.fourier_fft(x.werte[start:],y.werte[start:])
    fpeak_fft = analyse.peak(freq_fft,amp_fft, 1000, 2000)
    return fpeak_fft

def get_all_peaks(material):
    peaks_fft = []
    cassy_dir = "../../Messungen/"
    global start_values
    start_values = {"Kupfer_Einsp_Fehler_01": 5000,
                    "Kupfer_Messung_03":4500,
                    "Kupfer_Messung_04":5000,
                    "Kupfer_Messung_06":5000,
                    "Kupfer_Messung_07":5000,
                    "Kupfer_Messung_09":5000,
                    "Messing_Messung_06":5000,
                    "Messing_Messung_07":5000,
                    "Stahl_Messung_01":2000,
                    "Stahl_Messung_09":5000,
                    } # Der Startwert / 10000 ergibt die Startsekunde
     
    for dirpath, dirnames, filenames in os.walk(cassy_dir):
        for filename in filenames:
            if filename.endswith((".labx")) and material in filename:
                peaks_fft.append(fft_peak(cassy_dir + filename, "t", "U_A1", filename))


    Peaks_FFT_NP = np.array(peaks_fft)
    return Peaks_FFT_NP

Messing_F = get_all_peaks("Messing_Messung")
Kupfer_F =  get_all_peaks("Kupfer_Messung")
Stahl_F = get_all_peaks("Stahl_Messung")
Alu_F = get_all_peaks("Alu_Messung")

frequencies = {"Aluminium": Alu_F, "Messing": Messing_F, "Kupfer": Kupfer_F, "Stahl": Stahl_F}
print(pd.DataFrame(frequencies))
 

global PLOTS_DIR #Ordner, in dem die Plots gespeichert werden sollen, mit passender Martrikelnummer und Versuchnummer
PLOTS_DIR = '../plots/434170_428396_1A3_'
 
def plot_errorbar(x, y, yerr, plotname):
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.linewidth'] = 0.75
    plt.rcParams['lines.linewidth'] = 0.5
     
    fig, ax = plt.subplots()
    x = np.array(x)
    y = np.array(y)
    #TODO make fontsize smaller
    # TODO dots smaller
    # TODO achsenbeschriftung y aachse apsolute werte.
    yerr = np.array(yerr)
    plt.errorbar(x, y, yerr=yerr, fmt='.', markersize=5, capsize=2, capthick=0.8, elinewidth=1.5)
    plt.ylabel("f / Hz")
    plt.autoscale()
    formatter = ticker.ScalarFormatter(useOffset=False)
    ax.yaxis.set_major_formatter(formatter)
    plt.title(x[0] + " mit stat. Fehler " + str(yerr[0]) + " Hz")
    ax.yaxis.set_label_coords(-0.1, 1.09)
    plt.grid()
    plt.savefig(PLOTS_DIR + plotname + ".pdf")

 
# systematischer fehler auf Alu, Messing, Kupfer, Stahl
A_err = 0.03 
M_err = 0.03
K_err = 0.03
S_err = 0.03

x = ["Aluminium"] * len(Alu_F) +  ["Messing"] * len(Alu_F) + ["Kupfer"] * len(Alu_F) + ["Stahl"] * len(Alu_F)
y = np.concatenate((Alu_F, Messing_F, Kupfer_F, Stahl_F))
y_err =  np.concatenate((A_err * np.ones(len(Alu_F)), M_err * np.ones(len(Alu_F)), K_err * np.ones(len(Alu_F)), S_err * np.ones(len(Alu_F))))
print(y_err)
for i in range(0, 40, 10):
    plot_errorbar(x[i:i+10] , y[i:i+10], y_err[i:i+10], "frequenzen_stat_err_" + x[i])
 
# Erwartungswert und Standardabweichung
nachkommer_stellen = 3
Messing_F_mean = np.mean(Messing_F)
M_F_sigma = np.std(Messing_F,ddof=1)
M_err = M_F_sigma/np.sqrt(len(Messing_F))


print("Messing", Messing_F_mean)
print("Error auf Messing Frequenz:", round(M_err, nachkommer_stellen))

Kupfer_F_mean = np.mean(Kupfer_F)
K_F_sigma = np.std(Kupfer_F,ddof=1)
K_err = K_F_sigma/np.sqrt(len(Kupfer_F))

print("Kupfer", Kupfer_F_mean)
print("Fehler auf Kupfer:", round(K_err, nachkommer_stellen))

Stahl_F_mean = np.mean(Stahl_F)
S_F_sigma = np.std(Stahl_F,ddof=1)
S_err = S_F_sigma/np.sqrt(len(Stahl_F))

print("Stahl:", Stahl_F_mean)
print("Error auf Stahl Frequenz:", round(S_err, nachkommer_stellen))

Alu_F_mean = np.mean(Alu_F)
A_F_sigma = np.std(Alu_F,ddof=1)
A_err = A_F_sigma/np.sqrt(len(Alu_F))

print("Aluminium:", Alu_F_mean)
print("error auf Frequenz Alu:", round(A_err, nachkommer_stellen))

## Die tabelle im latex format, damit ich nichts abtippen muss :D
for i in range(len(Alu_F)):
    print("Nr. " + str(i + 1) + " & " + str(round(Stahl_F[i], 2)) + "Hz & " + str(round(Alu_F[i], 2)) + "Hz & " + str(round(Messing_F[i], 2)) + "Hz & " + str(round(Kupfer_F[i], 2)) + "Hz \\\\")
