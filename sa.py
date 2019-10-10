#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program usses Simulated Annealing to find the closest maximum to
# the starting location of the sum of gaussian function given generated based
# on the random seed number, number of dimensions, and number of centers (hills)

import SumofGaussians as SG
import numpy as np, sys

np.set_printoptions(formatter={'float': lambda x: "{0:0.8f}".format(x)}) # set printing format

seed = int(sys.argv[1]) #random number seed
dims = int(sys.argv[2]) #number of dimensions
ncenters = int(sys.argv[3]) #number of hills

np.random.seed(seed) #seed the numpy random number generator
sog = SG.SumofGaussians(dims,ncenters) #create the sum of gaussian function

iterations = 1 # starting iteration
temperature = 1.0 # starting temperature
alpha = 0.9999 # alpha used for decreasing the temperature

start = 10.0 * np.random.ranf(dims) #starting point
# perform simulated annealing
current = start

# while the tempearture is above the minimum tolerance and the
# iterations are less than the maximum number of iterations
# keep searching
while iterations <= 100000:
    #print the current location and the value of its point
    print(str(current).lstrip('[').rstrip(']'), "{:.8f}".format(sog.Eval(current)))
        
    # new random locaiton
    new_point = current + np.random.uniform(-0.01, 0.01, dims)
                
    # get a random number for comparing with probability
    random = np.random.uniform(0, 1)
    # calculate the difference between the new point and the old point
    delta = float(sog.Eval(new_point) - sog.Eval(current))
    # calculate the probability
    probability = np.exp(delta / temperature)
    
    # accept the new point if it is greater than the old location
    # or accept the new point as a bad move based on the probability
    if sog.Eval(new_point) > sog.Eval(current) or probability > random:
        current = new_point
        
    # decrease the tempearture slightly and increment the iteration
    temperature = (1.0 * alpha) ** (iterations)
    iterations += 1

# print the final point and its value
print(str(current).lstrip('[').rstrip(']'), "{:.8f}".format(sog.Eval(current)))  

#print("%.8f"%(sog.Eval(current)))
sys.exit(0)
