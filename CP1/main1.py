# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:44:57 2020

@author: natal
"""

import numpy as np

from setup import histories, slab, mid, Sigma_a, Sigma_c, Sigma_f, Sigma_s, Sigma_t
from col_type import col_type

captures=0
fissions=0
exits=0

track_lenghts=np.zeros(histories) #maybe I don't need this?
col_save=[] #to store collision locations

for n in range(histories):
    print('new history')
    track=0 #track length of each history
    
    #sample position and direction
    pos=slab*np.random.rand()
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
            track=track+dist_bound    
            print('boundary crossing')
            if reg==0 and direc==0: #in left region and moving left - will cross L edge
                active=False #neutron leaves slab by left edge
                print('leaves by left')
                exits=exits+1
            elif reg==0 and direc ==1: #in left region and moving right - will cross region boundary
                pos=mid+1e-10 #define new position (it can't be exactly on the border because it must be in one material or the other)
                print('new position')
            elif reg==1 and direc==0: #in right region and moving left - will cross region boundary
                pos=mid-1e-10 #define new position
                print('new position')
            else:                   #in right region and moving right
                active=False #neutron leaves slab by right edge
                print('leaves by right')
                exits=exits+1

        else:   #collision 
            track=track+dist_col
            col_save.append(pos)
            print('collision')
            #determine type of collision
            collision=col_type(reg) #0=capture, 1=fission, 2=scatter
            
            if collision==0:
                print('capture')
                active=False
                captures=captures+1
            elif collision==1:
                print('fission')
                #record position
                active=False
                fissions=fissions+1
            else: 
                print('scatter')
                #determine new direction: assume isotropic, so both directions are equally likely
                direc=np.random.randint(0,2) #0=going left, 1=going right
        
        # print('do the loop again')
    track_lenghts[n]=track 

col_loc=np.vstack(col_save)
# flux=sum(track_lenghts)/(histories*slab) 