# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 02:13:44 2020

@author: natal
"""

import numpy as np
import matplotlib.pyplot as plt
from setup import cycles, inactive_cycles

plt.rcParams['mathtext.default'] = 'regular'
plt.rcParams.update({'font.size': 20})  #general font size (axis labels)
plt.rc('legend', fontsize=12)    # legend fontsize
plt.rc('axes', linewidth=2) #thickness of axis lines

keff=np.loadtxt('keff')

plt.plot(keff)
plt.xlim(0,cycles-1)
plt.ylim(1.125,1.225)
plt.xlabel('Cycle #')
plt.ylabel('Multiplication factor')
plt.grid()

k_res=np.mean(keff[inactive_cycles:]) #k result
print('The multiplication factor is '+str(k_res))