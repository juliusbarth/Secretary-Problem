# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:19:01 2020

@author: jfb2444
"""
# Imports
import numpy as np
from math import e
import matplotlib.pyplot as plt

# Monte Carlo Simulation to find best strategy
def runMonteCarloSimulation(n, nbRep):   
    print("Running Simulation Optimization")
    nbStrategies = 99       # No. of strategies to test 
    strategies = np.linspace(1/(nbStrategies+1),1-1/(nbStrategies+1),nbStrategies)  
    successCount = np.zeros((nbStrategies))    # No. of replications where a given strategy results in a success
    successProb = np.zeros((nbStrategies))    # No. of replications where a given strategy results in a success
    for rep in range(0,nbRep):
        #print("--> Replication", rep,"( n =", n, ")")    
        np.random.seed(rep)
        candidateList = np.random.permutation(n)
        #print(candidateList)
        s = 0   # Strategy index
        # Strategy: fraction of candidates to explore before making decision
        for r in strategies:
            choiceRank = np.NaN
            # Simulate strategy for given random input data
            for i in  range(0,n):
                # Check if longer in exploration phase, i.e. in optimization phase
                if i+1 > r*n:
                    # If current candidate is better than all previous candiates:
                    # STOP! and choose this candidate.
                    if candidateList[i] == min(candidateList[0:i+1]):
                        choiceRank = candidateList[i]
                        break
                    elif i == n-1:
                        choiceRank = candidateList[i]
            if choiceRank == 0:
                #print("Success!")
                successCount[s] = successCount[s] + 1
            s = s + 1   # Update strategy index
            
    # Calculate success probability of each strategy for the simulated samples 
    successProb = [tmpElem / nbRep for tmpElem in successCount]
    
    # Find best strategy based on in-sample performance
    bestStrategy = strategies[successProb.index(max(successProb))]
    #print("Best strategy is r =", strategies[successProb.index(max(successProb))])
    
    # Plot perfomrance by strategy
    if False:
        plt.plot(strategies, successProb, label='MC Simulation Optimization') 
        plt.scatter(1/e, 1/e, marker='x', color='r', label='Theoretical optimum for large n')   
        plt.xlabel("Policy Threshold")
        plt.ylabel("Success Probability") 
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
    return bestStrategy

