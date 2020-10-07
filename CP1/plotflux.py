# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 02:06:27 2020

@author: natal
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['mathtext.default'] = 'regular'
plt.rcParams.update({'font.size': 20})  #general font size (axis labels)
plt.rc('legend', fontsize=12)    # legend fontsize
plt.rc('axes', linewidth=2) #thickness of axis lines

flux=np.loadtxt('flux')
bins=np.loadtxt('fluxbins')

plt.plot(bins,flux[:,-1])
# leg=plt.legend()    #whatever legend commands you need
# leg.set_title('Neutron Energy (keV)', prop = {'size':12})   #legend title font size
# leg.get_frame().set_linewidth(2)    #thickness of legend border
# leg.get_frame().set_edgecolor("black")  #legend border color
plt.xlim(0,100)
# plt.ylim(1,1e4)
plt.xlabel('Position (cm)')
plt.ylabel('# neutrons')
# plt.title('Pulse Integral Distribution')
plt.grid()
plt.minorticks_on()
plt.tick_params('both', length=10, width=2, which='major')  #axis major tick marks on both axes
plt.tick_params('both', length=8, width=1, which='minor')   #axis minor tick marks on both axes