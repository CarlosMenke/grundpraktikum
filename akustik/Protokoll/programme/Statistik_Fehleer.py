import numpy as np
import pandas as pd
import os
from praktikum import cassy, analyse
import matplotlib.pyplot as plt

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
#print(Alu_stdabw, 'Standardabweichung des Durchmessers von Alu')
#print((Alu_err, 'Fehler auf den Durchmesser der Aluminiumstange'))


#Berechnung des Mittelwerts der dichte
De =[Alu_err, M_err, K_err, S_err]
D = [Alu_mean, M_mean, K_mean, S_mean]
M = [0.4609, 1.4275, 1.5054, 1.3274]
L = 1.5

def roh(D, M, L):
    #print(D,M,L)
    roh = M/(np.pi*(D/2)**2*L)
    return roh
rho = []
for i, j in zip(D, M):
    p = roh(i, j, L)
    if i == Alu_mean:
        print("Dichte von Aluminium:", f"{p:.2f}" )
        rho.append(p)
    if i == M_mean:
        print("Dichte von Messing", f"{p:.2f}")
        rho.append(p)
    if i == K_mean:
        print("Dichte von Kupfer", f"{p:.2f}")
        rho.append(p)
    if i == S_mean:
        print("Dichte von Stahl15", f"{p:.2f}")
        rho.append(p)

print(rho)
 # Fehlerfortplanzung des Statistischen Fehlers auf die Dichte 

stat_rho = []
       
def sigma_roh(D, M, L, De):
    s = ((8*M)/(np.pi*D**3*L))**2*De**2
    return s

for i, j, k in zip(D, M, De):
    roh_err = np.sqrt(sigma_roh(i, j, L, k))
    if i == Alu_mean:
        print("stat. Fehler auf Dichte von Aluminium:", f"{roh_err:.2f}" )
        stat_rho.append(roh_err)
    if i == M_mean:
        print("stat. Fehler auf Dichte von Messing", f"{roh_err:.2f}")
        stat_rho.append(roh_err)
    if i == K_mean:
        print("stat. Fehler auf Dichte von Kupfer", f"{roh_err:.2f}")
        stat_rho.append(roh_err)
    if i == S_mean:
        print("stat. Fehler auf Dichte von Stahl15", f"{roh_err:.2f}")
        stat_rho.append(roh_err)

print(stat_rho)

Dee = 0.00001
Me = 0.0002
Le = 0.0007

syst_rho = []

def lin_err(D, M, L, Dee, Me, Le):
    delt = abs(((-1)*8*M)/(np.pi*D**3*L)*Dee)+abs(4/(np.pi*D**2*L)*Me)+abs(((-1)*4*M)/(np.pi*D**2*L**2)*Le)
    return delt

for i, j in zip(D, M):
    delt_roh = np.sqrt(lin_err(i, j, L, Dee, Me, Le))
    if i == Alu_mean:
        print("syst. Fehler auf Dichte von Aluminium:", f"{delt_roh:.2f}" )
        syst_rho.append(delt_roh)
    if i == M_mean:
        print("syst. Fehler auf Dichte von Messing", f"{delt_roh:.2f}")
        syst_rho.append(delt_roh)
    if i == K_mean:
        print("syst. Fehler auf Dichte von Kupfer", f"{delt_roh:.2f}")
        syst_rho.append(delt_roh)
    if i == S_mean:
        print("syst. Fehler auf Dichte von Stahl15", f"{delt_roh:.2f}")
        syst_rho.append(delt_roh)

print(syst_rho)



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
    plt.figure()
    x = np.array(x)
    y = np.array(y)
    #TODO make fontsize smaller
    # TODO dots smaller
    # TODO achsenbeschriftung y aachse apsolute werte.
    yerr = np.array(yerr)
    plt.errorbar(x, y, yerr=yerr, fmt='.')
    plt.xlabel("Category")
    plt.ylabel("f / Hz")
    plt.title("Frequenzen der Messungen mit Fehlerbalken")
    plt.grid()
    plt.savefig(PLOTS_DIR + plotname + ".pdf")

 
A_err = 0.003 
M_err = 0.003
K_err = 0.003
S_err = 0.003

x = ["Aluminium"] * len(Alu_F) +  ["Messing"] * len(Alu_F) + ["Kupfer"] * len(Alu_F) + ["Stahl"] * len(Alu_F)
y = np.concatenate((Alu_F, Messing_F, Kupfer_F, Stahl_F))
y_err =  np.concatenate((Alu_err * np.ones(len(Alu_F)), M_err * np.ones(len(Alu_F)), K_err * np.ones(len(Alu_F)), S_err * np.ones(len(Alu_F))))
for i in range(0, 40, 10):
    plot_errorbar(x[i:i+10] , y[i:i+10], y_err[i:i+10], x[i])
 
print(get_all_peaks("Messing"))
print(get_all_peaks("Kupfer_Messung"))

nachkommer_stellen = 3

f = []
stat_f = []

Alu_F_mean = np.mean(Alu_F)
A_F_sigma = np.std(Alu_F,ddof=1)
A_err = A_F_sigma/np.sqrt(len(Alu_F))
f.append(Alu_F_mean)
stat_f.append(A_err)
print("Aluminium:", Alu_F_mean)
print("error auf Frequenz Alu:", round(A_err, nachkommer_stellen))

Messing_F_mean = np.mean(Messing_F)
M_F_sigma = np.std(Messing_F,ddof=1)
M_err = M_F_sigma/np.sqrt(len(Messing_F))
f.append(Messing_F_mean)
stat_f.append(M_err)
print("Messing", Messing_F_mean)
print("Error auf Messing Frequenz:", round(M_err, nachkommer_stellen))

Kupfer_F_mean = np.mean(Kupfer_F)
K_F_sigma = np.std(Kupfer_F,ddof=1)
K_err = K_F_sigma/np.sqrt(len(Kupfer_F))
f.append(Kupfer_F_mean)
stat_f.append(K_err)
print("Kupfer", Kupfer_F_mean)
print("Fehler auf Kupfer:", round(K_err, nachkommer_stellen))

Stahl_F_mean = np.mean(Stahl_F)
S_F_sigma = np.std(Stahl_F,ddof=1)
S_err = S_F_sigma/np.sqrt(len(Stahl_F))
f.append(Stahl_F_mean)
stat_f.append(S_err)
print("Stahl:", Stahl_F_mean)
print("Error auf Stahl Frequenz:", round(S_err, nachkommer_stellen))

#print(f)
#print(stat_f)

## Die tabelle im latex format, damit ich nichts abtippen muss :D
#for i in range(len(Alu_F)):
    #print("Nr. " + str(i + 1) + " & " + str(round(Stahl_F[i], 2)) + "Hz & " + str(round(Alu_F[i], 2)) + "Hz & " + str(round(Messing_F[i], 2)) + "Hz & " + str(round(Kupfer_F[i], 2)) + "Hz \\\\")

D = [Alu_mean, M_mean, K_mean, S_mean]


def E(f,L,rho):
    E = (2*L*f)**2*rho
    return E

for i, k in zip(f, rho):
    E_Modul = E(i, L, k)
    if i == Alu_F_mean:
        print("E-Modul von Aluminium:", f"{E_Modul:.2f}" )
    if i == Messing_F_mean:
        print("E-Modul von Messing", f"{E_Modul:.2f}")
    if i == Kupfer_F_mean:
        print("E-Modul von Kupfer", f"{E_Modul:.2f}")
        rho.append(p)
    if i == Stahl_F_mean:
        print("E-Modul von Stahl15", f"{E_Modul:.2f}")
        rho.append(p) 
 
def sigma_E(f, L, rho, re, fe):
    s = 8*L**2*f*rho
    return s
