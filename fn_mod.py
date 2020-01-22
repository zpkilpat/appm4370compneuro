#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fn_mod.py

simulates and plots traces from fitzhugh-nagumo model with cubic thresholds at
0, 1/2, and 1
"""

import numpy as np
import matplotlib.pyplot as plt

ep = 0.01   # adaptation rate
g = 0.1       # adaptation strength
I=1         # input stimulus current

T = 100      # total time to run
dt = 0.01   # time step
nt = int(np.round(T/dt)+1)     # number of entries in vector array (mV)
tvec = np.linspace(0,T,nt)     # time vector (ms)

u = np.zeros(nt)   # vector of voltage entries
w = np.zeros(nt)   # vector of adaptation variable entries

for j in np.arange(nt-1):
    u[j+1] = u[j]+dt*(u[j]*(u[j]-1/2)*(1-u[j])-w[j]+I)
    w[j+1] = w[j]+dt*(ep*(u[j]-g*w[j]))

 
# plot commands
fig = plt.figure()       
plt.plot(tvec,u,linewidth=4.0)
plt.plot(tvec,w,linewidth=4.0)
plt.xlabel('time')
plt.ylabel('voltage/adaptation')
plt.show()
fig.savefig('fn_model_tser.png', dpi=fig.dpi)
fig = plt.figure()     
  
plt.plot(u,w,linewidth=4.0)
plt.xlabel('voltage, u')
plt.ylabel('adaptation, w')
plt.show()
fig.savefig('fn_model_pplane.png', dpi=fig.dpi)
