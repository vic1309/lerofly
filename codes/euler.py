
#######################################################
### Programa utilizado para aproximar numericamente ###
### a seguinte ODE:                                 ###
###                                                 ###
###     dy/dt = 3 + e^(-t) - 1/2*y, y(0) = 1        ### 
###                                                 ###
### Utilizado o Metodo de Euler:                    ###
### y[n+1] = y[n] +f(t[n], y[n])*(t[n+1] - t[n])    ###
### ----------------------------------------------- ###
### "Equacoes Diferenciais Elementares e Problemas  ###
###   de Valores de Contorno" - Boyce & Diprima     ###   
###   8º Ed. Cap: 2.7, Exemplo: 1                   ###
### ----------------------------------------------- ###
#######################################################

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
fig, ax = plt.subplots() 

dt = [0.1, 0.05, 0.025, 0.01]
f0 = 1 # Initial condition
tn = 5 # Size of grid

for i in dt:
    dt  = i # Time interval (0.5, 2) --- 
    N_t =  int(tn/dt) # N_t = tn/dt -- Number of meshgrid points

    from numpy import linspace, zeros, exp
    t = linspace(0, (N_t)*dt, N_t+1)
    y = zeros(N_t+1)
    f = zeros(N_t+1)

    y[0] = f0

    for n in range(N_t):
        f[n] = 3 + np.exp(-t[n]) - (1/2)*y[n]
        #print(f[n])
        y[n+1] = y[n] + dt*f[n]

    ax.plot(t, y, label = 'dt = %s'%("{0:.3f}".format(i)))

###########################
### Analytical solution ###
###########################

ta = np.arange(0, tn+1, 1)
ya = 6 - 2*np.exp(-ta) - 3*np.exp(-ta/2)

ax.plot(ta, ya, color='lawngreen', label = 'exact')

plt.yticks(np.arange(0, 7, 1))
plt.xticks(np.arange(0, 7, 1))

#####################
### Legend format ###
#####################

legend_properties = {'weight':'semibold',
'size':8}

### Organize labels ### 

leg = ax.legend(loc=2, prop=legend_properties)

### Set linewdith separately from lines plotted ###
for line in leg.get_lines():
    line.set_alpha(1)

frame = leg.get_frame()
frame.set_color('gainsboro')

plt.xlabel('t', size = 12, weight = 'semibold'); 
plt.xticks(size = 10, weight = 'semibold')

plt.ylabel(u'$y(t)$', size = 14, weight = 'semibold')
plt.yticks(size = 10, weight = 'semibold')
