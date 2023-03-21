import numpy as np
import matplotlib.pyplot as plt
import praktikum as p
from praktikum import cassy
from praktikum import analyse

plt.rcParams['font.size'] = 24.0
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelsize'] = 'medium'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.linewidth'] = 1.2
plt.rcParams['lines.linewidth'] = 2.0



data = cassy.CassyDaten('M1_Stange.labx')
data = cassy.CassyDaten('M2_Stange.labx')
data = cassy.CassyDaten('M3_Stange.labx')
data = cassy.CassyDaten('M1_Stange_Pendelkörper.labx')
data = cassy.CassyDaten('M2_Stange_Pendelkörper.labx')
data = cassy.CassyDaten('M3_Stange_Pendelkörper.labx')

U_1   = data.messung(1).datenreihe('U_B1').werte 
t_1   = data.messung(1).datenreihe('t').werte 
U_2   = data.messung(1).datenreihe('U_B1').werte 
t_2   = data.messung(1).datenreihe('t').werte 
U_3   = data.messung(1).datenreihe('U_B1').werte 
t_3   = data.messung(1).datenreihe('t').werte 
U_4   = data.messung(5).datenreihe('U_B1').werte 
t_4    = data.messung(5).datenreihe('t').werte 
U_5   = data.messung(6).datenreihe('U_B1').werte 
t_5    = data.messung(6).datenreihe('t').werte
U_6   = data.messung(7).datenreihe('U_B1').werte 
t_6    = data.messung(7).datenreihe('t').werte  

fig, ax = plt.subplots(1, 1, figsize=(10,8),sharex=True)
ax.axhline(0,color='black',linestyle = '--', lw=1)
ax.plot(t_1,U_1, color = 'r')
ax.set_ylabel('$U$ / V')
ax.set_xlabel('$t$ / s')

fig, ax = plt.subplots(1, 1, figsize=(10,8),sharex=True)
ax.axhline(0,color='black',linestyle = '--', lw=1)
ax.plot(t_2,U_2, color = 'r')
ax.set_ylabel('$U$ / V')
ax.set_xlabel('$t$ / s')

fig, ax = plt.subplots(1, 1, figsize=(10,8),sharex=True)
ax.axhline(0,color='black',linestyle = '--', lw=1)
ax.plot(t_3,U_3, color = 'r')
ax.set_ylabel('$U$ / V')
ax.set_xlabel('$t$ / s')

fig, ax = plt.subplots(1, 1, figsize=(10,8),sharex=True)
ax.axhline(0,color='black',linestyle = '--', lw=1)
ax.plot(t_4,U_4, color = 'r')
ax.set_ylabel('$U$ / V')
ax.set_xlabel('$t$ / s')

fig, ax = plt.subplots(1, 1, figsize=(10,8),sharex=True)
ax.axhline(0,color='black',linestyle = '--', lw=1)
ax.plot(t_5,U_5, color = 'r')
ax.set_ylabel('$U$ / V')
ax.set_xlabel('$t$ / s')

fig, ax = plt.subplots(1, 1, figsize=(10,8),sharex=True)
ax.axhline(0,color='black',linestyle = '--', lw=1)
ax.plot(t_6,U_6, color = 'r')
ax.set_ylabel('$U$ / V')
ax.set_xlabel('$t$ / s')

fig, ax = plt.subplots(1, 1, figsize=(10,8),sharex=True)
ax.axhline(0,color='black',linestyle = '--', lw=1)
ax.scatter(t_1[0:500],U_1[0:500], color = 'r')
ax.set_ylabel('$U$ / V')
ax.set_xlabel('$t$ / s')






plt.show()