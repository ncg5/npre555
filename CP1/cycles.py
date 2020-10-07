# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:44:57 2020

@author: natal
"""

import numpy as np
import matplotlib.pyplot as plt

from setup import cycles, nu, histories, slab, mid, Nbins, Sigma_t
from col_type import col_type

k_save=np.zeros(cycles)
flux_save=np.zeros((Nbins,cycles))

fis_loc=slab*np.random.rand(histories) #fission locations. Start with a random distribution of locations for new particles

for m in range(cycles):

    col_save=[] #to store collision locations 
    fis_save=[] #to store fission locations
    fissions=0 #number of fissions in the current cylce
    
    for n in range(histories):        
        #sample position and direction
        pos=fis_loc[np.random.randint(0,len(fis_loc))]
        direc=np.random.randint(0,2) #0=going left, 1=going right
        #Because this problem is 1D, the only sense of an angle that we need is whether the neutron is moving right or left
    
        active=True #use this to tell the code when to end a history
    
        while active==True:
            if pos<mid:
                reg=0 #which region the neutron is in: 0=left, 1=right. Will use this to index cross sections
            else:
                reg=1
            
            #determine distance to boundary
            if reg==0 and direc==0: #in left region and moving left - will cross L edge
                dist_bound=pos #disante to left boundary = the neutron position
            elif reg==0 and direc ==1: #in left region and moving right - will cross region boundary
                dist_bound=mid-pos 
            elif reg==1 and direc==0: #in right region and moving left - will cross region boundary
                dist_bound=pos-mid
            else:                   #in right region and moving right
                dist_bound=slab-pos
            
            #determine distance to collision
            xi_col=np.random.rand() #generate a random number xi
            dist_col=-np.log(1-xi_col)/Sigma_t[reg]
            
            #determine next event
            if dist_bound<dist_col: #crosses boundary   
                if reg==0 and direc==0: #in left region and moving left - will cross L edge
                    active=False #neutron leaves slab by left edge
                elif reg==0 and direc ==1: #in left region and moving right - will cross region boundary
                    pos=mid+1e-10 #define new position (it can't be exactly on the border because it must be in one material or the other)
                elif reg==1 and direc==0: #in right region and moving left - will cross region boundary
                    pos=mid-1e-10 #define new position
                else:                   #in right region and moving right
                    active=False #neutron leaves slab by right edge
    
            else:   #collision 
                if pos not in col_save: #don't count scatters in same location
                    col_save.append(pos)
                #determine type of collision
                collision=col_type(reg) #0=capture, 1=fission, 2=scatter
                
                if collision==0:
                    active=False
                elif collision==1:
                    active=False
                    fissions=fissions+1
                    #record position
                    fis_save.append(pos)
                else: 
                    #determine new direction: assume isotropic, so both directions are equally likely
                    direc=np.random.randint(0,2) #0=going left, 1=going right
    
    col_loc=np.vstack(col_save)
    fis_loc=np.vstack(fis_save)
    
    #sort collision locations into a histogram to get phi(x)
    col_hist, flux_bin_edges=np.histogram(col_loc,bins=Nbins,range=(0,slab)) 
    flux_bins=(flux_bin_edges[0:-1]+flux_bin_edges[1:])/2
    flux_save[:,m]=col_hist
    # plt.plot(flux_bins,col_hist)
    
    #calculate k_eff
    k=nu*fissions/histories    
    k_save[m]=k
    
np.savetxt('keff',k_save)
np.savetxt('flux',flux_save)
np.savetxt('fluxbins',flux_bins)

