# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:24:19 2020

@author: natal
"""

#NPRE 555 CP 1
#This file contains the necessary information to setup the problem, like geometry and material definitions

histories=1

#geometry
slab=100 #slab thickness in cm
mid=50 #location of region boundary in cm

#material properties
nu=2.4
#region 1 (left side, 0<x<mid)
Sigma_a1=0.12 #absorption (cm-1) 
Sigma_s1=0.05 #scattering
Sigma_f1=0.15/nu #fission
Sigma_c1=Sigma_a1-Sigma_f1 #capture 
Sigma_t1=Sigma_a1+Sigma_s1 #total
#region 2 (right side, mid<x<slab)
Sigma_a2=0.10 #cm-1
Sigma_s2=0.05
Sigma_f2=0.12/nu
Sigma_c2=Sigma_a2-Sigma_f2 
Sigma_t2=Sigma_a2+Sigma_s2

Sigma_a=[Sigma_a1,Sigma_a2]
Sigma_c=[Sigma_c1,Sigma_c2]
Sigma_f=[Sigma_f1,Sigma_f2]
Sigma_s=[Sigma_s1,Sigma_s2]
Sigma_t=[Sigma_t1,Sigma_t2]