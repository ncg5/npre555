# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:00:02 2020

@author: natal
"""

#NPRE 555 CP 1
#workflow outline

import numpy as np

#histories=10 #number of histories/cycles to run
from setup import histories, slab, mid, Sigma_a, Sigma_c, Sigma_f, Sigma_s, Sigma_t  


for n in range(histories):
    #STEP 1: new particle: sample position, energy, and angle
    pos=slab*np.random.rand() #position (x-coordinate) in cm
    if pos<mid:
        reg=0 #will use this to index cross sections
    else:
        reg=1
    
    #sample energy from chi distribution - Do I need this?
    #sample angle isotropically - Do I need this?
    ang=2*np.pi*np.random.rand()
    mu=np.cos(ang)
    
    
    #STEP 2: determine distance to regional boundary
    #distance to left boundary (x=0) = pos
    dist_mid=np.absolute(pos-mid) #distance to region boundary in cm
    #maybe dont use absval here, but instead use it in "distances" so I can get new pos later
    dist_R=slab-pos #distance to right boundary (x=slab) in cm
    distances=[pos,dist_mid,dist_R]
    closest_bound=np.argmin(distances)
    dist_bound=distances[closest_bound]
    
    
    #STEP 3: determine distance to next collision
    xi_col=np.random.rand() #generate a random number xi
    # if pos<mid: #region 1
    #     dist_col=-np.log(1-xi_col)/Sigma_t1
    # else: #region 2
    #     dist_col=-np.log(1-xi_col)/Sigma_t2
    dist_col=-np.log(1-xi_col)/Sigma_t[reg]    
    
    #STEP 4: determine if a collison or boundary crossing happens first
    event_dist=[dist_bound, dist_col] 
    event_type=np.argmin(event_dist) #0=boundary crossing, 1=collision
    track_length=event_dist[event_type] #store the distance to collision
    #if event_type=0, pos gets adjusted then repeat from step 2
    
    # if event_type==1: #for collisions, determine the collision type
        #xi_coltype=np.random.rand() #generate a random number xi
        #make a function to determine collision type