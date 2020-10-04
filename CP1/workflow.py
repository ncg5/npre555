# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:00:02 2020

@author: natal
"""

#NPRE 555 CP 1
#workflow outline

import numpy as np

#geometry
a=1.0 #slab thickness in meters
a1=0.5 #location of region boundary

#material properties
#region 1 (left side, 0<x<a1)
nu=2.4
Sigma_a1=0.12 #cm-1
Sigma_s1=0.05
Sigma_f1=0.15/nu
Sigma_t1=Sigma_a1+Sigma_s1
#region 2 (right side, a1<x<a)
Sigma_a2=0.10 #cm-1
Sigma_s2=0.05
Sigma_f2=0.12/nu
Sigma_t2=Sigma_a2+Sigma_s2


#STEP 1: new particle: sample position, energy, and angle
pos=a*np.random.rand() #position (x-coordinate) in meters

#sample energy from chi distribution - Do I need this?
#sample angle isotropically - Do I need this?
ang=2*np.pi*np.random.rand()
mu=np.cos(ang)


#STEP 2: determine distance to regional boundary
#distance to left boundary (x=0) = pos
dist_a1=np.absolute(pos-a1) #distance to region boundary
dist_R=a-pos #distance to right boundary (x=a)
distances=[pos,dist_a1,dist_R]
closest_bound=np.argmin(distances)
dist_bound=distances[closest_bound]


#STEP 3: determine distance to next collision
xi_col=np.random.rand()
if pos<a1: #region 1
    dist_col=-np.log(1-xi_col)/Sigma_t1
else: #region 2
    dist_col=-np.log(1-xi_col)/Sigma_t2

