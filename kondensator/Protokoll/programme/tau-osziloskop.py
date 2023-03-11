import numpy as np
import pandas as pd

names_messung = ["1. Endladen am Wiederstand", "2. Endladen am Wiederstand", "1. Endladen am Kondensator", "2. Endladen am Kondensator",  "1. Aufladen am Wiederstand", "2. Aufladen am Wiederstand", "1. Aufladen am Kondensator", "2. Aufladen am Kondensator"]
t1 = np.array([0.0006, 0.0006, 0.0004, 0.0004, 0.0045, 0.0045, 0.0034, 0.0034])
t2 = np.array([0.0404, 0.0404, 0.0312, 0.0312, 0.0226, 0.0226, 0.0180, 0.0180])

U1 = np.array([6.64, 6.64, 6.76, 6.76, -4.08, -4.08, -2.16, -2.16])
#original offset
Uoff = np.array([0.02, 0, 0, 0, 0, 0, -7.22, -7.22])
# bessere offsets
Uoff = np.array([0.04, 0.002, 0, 0, 0, 0, -7.22, -7.22])
U2 = np.array([0.16, 0.16, 0.32, 0.32, -0.72, -0.68, -6.04, -6.04])

offsets1 = []
# berechnung von Tau
tau = (t1 - t2)/ np.log((U1-Uoff)/(U2-Uoff))
print(pd.DataFrame(tau, index=names_messung, columns=["Tau"]))


# andreas statistik
