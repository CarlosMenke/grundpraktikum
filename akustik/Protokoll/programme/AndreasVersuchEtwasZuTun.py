import numpy as np
import pandas as pd
import os
from praktikum import cassy, analyse

### Durchmesser der Stangen
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
 
'''print(get_all_peaks("Messing"))
print(get_all_peaks("Kupfer_Messung"))'''

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
#for i in range(len(Alu_F)):
    #print("Nr. " + str(i + 1) + " & " + str(round(Stahl_F[i], 2)) + "Hz & " + str(round(Alu_F[i], 2)) + "Hz & " + str(round(Messing_F[i], 2)) + "Hz & " + str(round(Kupfer_F[i], 2)) + "Hz \\\\")
