#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program uses greedy local search (gradient ascent) to find the closest maximum to the starting
# location of the sum of gaussian function given generated based on the random seed number, 
# number of dimensions, and number of centers (hills)

import SumofGaussians as SG
import numpy as np, sys
np.set_printoptions(formatter={'float': lambda x: "{0:0.8f}".format(x)}) # set printing format


seed = int(sys.argv[1]) #random number seed
dims = int(sys.argv[2]) #number of dimensions
ncenters = int(sys.argv[3]) #number of hills

np.random.seed(seed) #seed the numpy random number generator
sog = SG.SumofGaussians(dims,ncenters) #create the sum of gaussian function
delta = 1 #initialize delta
iterations = 1 # number of iterations
epsilon = 1e-8 #increase tolerance
    
current = 10.0 * np.random.ranf(dims) #start at a random point

# greedy local search while the difference between the old point and the new point
# is above the tolerance and the number of iterations is less than 100,000
while delta > epsilon and iterations <= 100000:
    #print the current location and the value of its point
    print(str(current).lstrip('[').rstrip(']'), "{:.8f}".format(sog.Eval(current)))
    iterations += 1
    
    # create a new point of the old point increased by the step size
    new = current + (0.01 * sog.Deriv(current))
    # calculate the difference in the new point vs the old point
    delta = abs(sog.Eval(new) - sog.Eval(current))
    # set current to the new location
    current = new

# print the final point and its value
print(str(current).lstrip('[').rstrip(']'), "{:.8f}".format(sog.Eval(current))) 


#print("%.8f"%(sog.Eval(current)))
sys.exit(0)
    
