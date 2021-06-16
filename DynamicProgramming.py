# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:55:26 2020

@author: jfb2444
"""
import numpy as np   
 
                     
def runDynamicProgramming(n):
    
    print("Running Dynamic Programming Algorithm")

    # value of being in period k and state s
    value = np.empty((n,2))       # 1: current is best so far, 0: current is not best so far
    value[:] = np.NaN
    
    # Optimal action in period k and state s
    action = np.empty((n,2))       # 1: pick, 0: don't pick
    action[:] = np.NaN
    
    K_index = range(0,n)
    
    for k_index in reversed(K_index):
        k = k_index+1
        if k == n:
            value[k_index][1] = 1
            value[k_index][0] = 0
            action[k_index][1] = 1
            action[k_index][0] = 1
        else:
            for s in {0,1}:
                if s == 0: # Optimization Problem when current candidate is not ranked 1
                    tmpvalueStop = 0
                    tmpvalueCont = 1/(k+1) * value[k_index+1][1] + (k/(k+1)) * value[k_index+1][0]
                    value[k_index][s] =  max(tmpvalueStop, tmpvalueCont)
                    action[k_index][s] = 0
                if s == 1: # Optimization Problem when current candidate is ranked 1
                    tmpvalueStop = k/n
                    tmpvalueCont = 1/(k+1) * value[k_index+1][1] + (k/(k+1)) * value[k_index+1][0] 
                    value[k_index][s] =  max(tmpvalueStop, tmpvalueCont)
                    if tmpvalueStop > tmpvalueCont:
                        action[k_index][s] = 1
                    else:
                        action[k_index][s] = 0
    
    # Find optimal strategy
    for k_index in K_index:
        k = k_index+1
        if action[k_index][1] == 1:
            threshold_accept_abs = k-1  
            threshold_accept_rel = threshold_accept_abs/n
            break
        
    return threshold_accept_rel, threshold_accept_abs
