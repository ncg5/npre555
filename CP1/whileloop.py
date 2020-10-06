# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:17:20 2020

@author: natal
"""
import numpy as np

histories=1
for n in range(histories):
    #sample position and direction
    pos=np.random.rand()
    direc=np.random.randint(0,2)
    
    active=True #use this to tell the code when to end a history

    while active==True:
        #determine dist to boundary
        dist_bound=np.random.rand()
        #determine dist to collision
        dist_col=np.random.rand()
        #determine next event
        if dist_bound<dist_col:
            next_event=0 #crosses boundary
            print('leaves slab')
            active=False
        else:
            next_event=1 #collision
            print('collision')