import numpy as np
import scipy.odr
import matplotlib.pyplot as plt
import os
from praktikum import cassy, analyse

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
                    "Kupfer_Messung_03":5000,
                    "Kupfer_Messung_04":5000,
                    "Kupfer_Messung_06":5000,
                    "Kupfer_Messung_07":5000,
                    "Kupfer_Messung_09":5000,
                    "Messing_Messung_06":5000,
                    "Messing_Messung_07":5000,
                    "Stahl_Messung_01":5000,
                    "Stahl_Messung_09":5000,
                    } # Der Startwert / 10000 ergibt die Startsekunde
     
    for dirpath, dirnames, filenames in os.walk(cassy_dir):
        for filename in filenames:
            if filename.endswith((".labx")) and "Kupfer_Messung" in filename:
                peaks_fft.append(fft_peak(cassy_dir + filename, "t", "U_A1", filename))


    Peaks_FFT_NP = np.array(peaks_fft)
    return Peaks_FFT_NP
 
print(get_all_peaks("Kupfer"))
print(get_all_peaks("Stahl"))
