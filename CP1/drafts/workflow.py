# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:00:02 2020

@author: natal
"""

#NPRE 555 CP 1
#workflow outline

import numpy as np

from setup import histories, slab, mid, Sigma_a, Sigma_c, Sigma_f, Sigma_s, Sigma_t  
from col_type import col_type

captures=0
fissions=0
scatters=0
crossings=0

for n in range(histories):
    #STEP 1: new particle: sample position, energy, and angle
    pos=slab*np.random.rand() #position (x-coordinate) in cm
    if pos<mid:
        reg=0 #will use this to index cross sections
    else:
        reg=1
    
    #sample energy from chi distribution - Do I need this?
    #sample angle isotropically - Do I need this?
    xi_dir=np.random.rand()
    #Because this is a 1D problem, the only direction we need to worry about is left or right
    if xi_dir<0.5:
        direc=0 #indicates the neutron is moving in the -x direction
    else:
        direc=1 #indicates the neutron is moving in the +x direction
    # ang=2*np.pi*np.random.rand()
    # mu=np.cos(ang)
    
    
    #STEP 2: determine distance to any boundary
    if reg==0 and direc==0: #in left region and moving left - will cross L edge
        dist_bound=pos #disante to left boundary = the neutron position
    elif reg==0 and direc ==1: #in left region and moving right - will cross region boundary
        dist_bound=mid-pos 
    elif reg==1 and direc==0: #in right region and moving left - will cross region boundary
        dist_bound=pos-mid
    else:                   #in right region and moving right
        dist_bound=slab-pos 
    
    
    #STEP 3: determine distance to next collision
    xi_col=np.random.rand() #generate a random number xi
    dist_col=-np.log(1-xi_col)/Sigma_t[reg]    
    
    
    #STEP 4: determine if a collison or boundary crossing happens first
    event_dist=[dist_bound, dist_col] 
    event_type=np.argmin(event_dist) #0=boundary crossing, 1=collision
    track_length=event_dist[event_type] #store the distance to collision
    
    
    if event_type==0: #pos gets adjusted then repeat from step 2
        crossings=crossings+1
    if event_type==1: #for collisions, determine the collision type
        collision=col_type(reg)
        
        if collision==0: #capture
            captures=captures+1 
        if collision==1: #fission
            fissions=fissions+1
            #tally fission location
        if collision==2: #scattering
            scatters=scatters+1
            #sample new direction, then repeat steps 2-4
        
# print(captures+fissions+scatters+crossings)        