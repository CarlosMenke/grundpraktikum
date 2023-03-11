import numpy as np
import pandas as pd
import sympy as sp
#from sympy import symbo
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


global PLOTS_DIR #Ordner, in dem die Plots gespeichert werden sollen, mit passender Martrikelnummer und Versuchnummer
PLOTS_DIR = '../plots/434170_428396_1A3_'
 
names_messung = ["1. Endladen am Wiederstand", "2. Endladen am Wiederstand", "1. Endladen am Kondensator", "2. Endladen am Kondensator",  "1. Aufladen am Wiederstand", "2. Aufladen am Wiederstand", "1. Aufladen am Kondensator", "2. Aufladen am Kondensator"]
t1 = np.array([0.0006, 0.0006, 0.0004, 0.0004, 0.0045, 0.0045, 0.0034, 0.0034])
t2 = np.array([0.0404, 0.0404, 0.0312, 0.0312, 0.0226, 0.0226, 0.0180, 0.0180])

U1 = np.array([6.64, 6.64, 6.76, 6.76, -4.08, -4.08, -2.16, -2.16])
U2 = np.array([0.16, 0.16, 0.32, 0.32, -0.72, -0.68, -6.04, -6.04])
#original offset
Uoff = np.array([0.02, 0.02, 0.02, 0.02, -0.02, -0.02, -7.22, -7.22])
# bessere offsets
Uoff = np.array([0.04, 0.04, 0.04, 0.04, -0.04, -0.04, -7.22, -7.22])
 
offsets1 = []
# berechnung von Tau
tau = (t1 - t2)/ np.log((U1-Uoff)/(U2-Uoff)) * 1000
print(pd.DataFrame(tau, index=names_messung, columns=["Tau"]))
print(np.std(tau, ddof=1))

 
def plot_tau_errorbar(x, y, yerr, plotname):
    plt.rcParams['font.size'] = 12.0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.labelsize'] = 'medium'
    plt.rcParams['axes.linewidth'] = 0.75
    plt.rcParams['lines.linewidth'] = 0.5
     
    fig, ax = plt.subplots()
    plt.errorbar(x, y, yerr=yerr, fmt='.', markersize=8, capsize=2, capthick=0.8, elinewidth=1.5)
    plt.ylabel("U / V")
    plt.autoscale()
    formatter = ticker.ScalarFormatter(useOffset=False)
    ax.yaxis.set_major_formatter(formatter)
    plt.title("Messung mit dem Oszilloskop")
    ax.yaxis.set_label_coords(-0.1, 1.09)
    plt.grid()
    plt.savefig(PLOTS_DIR + plotname + ".pdf")

#TODO error auf tau einsetzten
y_err = np.array(0.04 * np.ones(len(tau)))
plot_tau_errorbar(names_messung, tau, y_err, "tau_errorbar")

# andreas statistik

t_1, t_2, U_1, U_2, U_o, U_0= sp.symbols('t_1 t_2 U_1 U_2 u_o U_0' , real=True)

ta = (t_1 -t_2)/(sp.ln((U_1-U_o)/(U_2-U_o)))
taA = (t_1 -t_2)/(sp.ln((U_0-U_1)/(U_0-U_1)))

sig_tau = (sp.diff(ta, t_1))
sp.pprint(sig_tau)
sp.pprint(sp.diff(ta, t_2))
sp.pprint(sp.diff(ta, U_1))
sp.pprint(sp.diff(ta, U_2))
#sp.pprint(sp.diff(ta, U_o))


'''
t_1, t_2, U_1, U_2, U_o, U_0= sp.symbols('t_1 t_2 U_1 U_2 u_o U_0' , real=True)

ta = (t_1 -t_2)/(sp.ln((U_1-U_o)/(U_2-U_o)))

sig_tau = (sp.diff(ta, t_1))
sp.pprint(sig_tau)




def sig_tau(t1, t2, U1, U2, Uo):
    a = sig_tau.subs(((t_1, t1), (t_2, t2), (U_1, U1), (U_2, U2), (U_o, Uo)))
    return a

print(sig_tau(1, 5, 4 ,3, 7))

def sig_tau(t1, t2, U1, U2, Uo, U0):
    a = ta.subs([(t_1, t1), (t_2, t2), (U_1, U1), (U_2, U2), (U_o, Uo), (U_0, U0)])
    return a

print(sig_tau(1, 5, 4 ,3, 4, 7))'''
