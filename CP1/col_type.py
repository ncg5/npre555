# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:03:27 2020

@author: natal
"""

#NPRE 555 CP 1
#function to determine collision type

import numpy as np

from setup import Sigma_c, Sigma_f, Sigma_s, Sigma_t

def col_type(reg):
    #normalize collision cross sections to total
    Cnorm=Sigma_c[reg]/Sigma_t[reg]
    Fnorm=Sigma_f[reg]/Sigma_t[reg]
    Snorm=Sigma_s[reg]/Sigma_t[reg]
    #make a discrete pdf to sample from
    C=Cnorm
    F=Cnorm+Fnorm
    S=Fnorm+Snorm #should =1
    xi=np.random.rand() #generate a random number xi
    if xi<C:
        col_type=0 #capture
    elif xi>C and xi<F: 
        col_type=1 #fission
    else:
        col_type=2 #scattering
    return(col_type)