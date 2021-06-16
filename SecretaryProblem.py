# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:57:21 2020

@author: jfb2444
"""

# Imports
import math
import matplotlib.pyplot as plt
from MonteCarloSimulation import runMonteCarloSimulation
from DynamicProgramming import runDynamicProgramming

# Pseudoclear console
for i in range(25):
    print("")

'''
TODO:
    - write up

'''

# Data
n_max = 50           # Max no. of candidates
nbRep = 500          # No. of replications for MC simulation optimization

n_values = range(0,n_max+1)

# Arrays to store results
sol_rel_Analytical = len(n_values)*[None]
sol_rel_MonteCarloSimulation = len(n_values)*[None]
sol_rel_MDP = len(n_values)*[None]
sol_abs_MDP = len(n_values)*[None]

# Find solution for given n
for n in n_values:
    if n >= 1:
        nbRep = int(round(math.log(math.factorial(n)),0))          # No. of replications for MC simulation optimization
        print("\nSolving for n =", n, "with", nbRep, "replications") 
        # Use analytical solution for large n as approximation
        sol_rel_Analytical[n] = 1/math.e
        # Run MDP to find best strategy
        sol_rel_MDP[n], sol_abs_MDP[n] = runDynamicProgramming(n)
        # Monte Carlo Simulation to find best strategy
        #sol_rel_MonteCarloSimulation[n] = runMonteCarloSimulation(n, nbRep)   
        
# PLot results
fig = plt.figure()
plt.plot(n_values, sol_rel_MDP, marker='.', color='r', label= ('Dynamic Programming') )
#plt.plot(n_values, sol_rel_MonteCarloSimulation, marker='.', color='g', label= ('MC Simulation Optimization (' + str(nbRep) + ' replications)') )  
plt.plot(n_values, sol_rel_Analytical, label='Asmymptotic result: 1/e')
plt.axis([0, max(n_values), -0.1, 1.1])
plt.grid(True)
plt.xlabel("n")
plt.ylabel("Policy Threshold") 
plt.legend() # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

