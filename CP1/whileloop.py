# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:17:20 2020

@author: natal
"""
import numpy as np

slab=1
mid=0.5
histories=1
for n in range(histories):
    #sample position and direction
    pos=np.random.rand()
    direc=np.random.randint(0,2) #0=going left, 1=going right
    #Because this problem is 1D, the only sense of an angle that we need is whether the neutron is moving right or left

    active=True #use this to tell the code when to end a history

    while active==True:
        if pos<mid:
            reg=0 #which region the neutron is in: 0=left, 1=right. Will use this to index cross sections
        else:
            reg=1
        
        #determine dist to boundary
        if reg==0 and direc==0: #in left region and moving left - will cross L edge
            dist_bound=pos #disante to left boundary = the neutron position
        elif reg==0 and direc ==1: #in left region and moving right - will cross region boundary
            dist_bound=mid-pos 
        elif reg==1 and direc==0: #in right region and moving left - will cross region boundary
            dist_bound=pos-mid
        else:                   #in right region and moving right
            dist_bound=slab-pos
        
        #determine dist to collision
        dist_col=np.random.rand()
        
        #determine next event
        if dist_bound<dist_col: #crosses boundary
            # next_event=0 
            print('boundary crossing')
            if reg==0 and direc==0: #in left region and moving left - will cross L edge
                active=False #neutron leaves slab by left edge
                print('leaves by left')
            elif reg==0 and direc ==1: #in left region and moving right - will cross region boundary
                pos=mid+1e-10 #define new position (it can't be exactly on the border because it must be in one material or the other)
                print('new position')
            elif reg==1 and direc==0: #in right region and moving left - will cross region boundary
                pos=mid-1e-10 #define new position
                print('new position')
            else:                   #in right region and moving right
                active=False #neutron leaves slab by right edge
                print('leaves by right')

        else:   #collision
            # next_event=1 
            print('collision')
            #determine type of collision
            det_col=np.random.randint(0,3)
            if det_col==0:
                print('capture')
                active=False
            elif det_col==1:
                print('fission')
                #record position
                active=False
            else: 
                print('scatter')
                #determine new direction: assume isotropic, so both directions are equally likely
                direc=np.random.randint(0,2) #0=going left, 1=going right
        
        print('do the loop again')