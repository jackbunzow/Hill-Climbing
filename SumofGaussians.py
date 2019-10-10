#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class SumofGaussians():
    def __init__(self,dimensions,number_of_centers):
        if (dimensions < 1 or number_of_centers < 1):
            self.centers = None
            return
        self.centers = np.array([np.random.ranf(dimensions) * 10.0 for i in range(number_of_centers)])
        return
    def Eval(self,point):
        return np.sum(np.exp(-np.sum(np.apply_along_axis(lambda x: (point - x)**2.0,1,self.centers),1)))
    def Deriv(self,point):
        return np.sum(-1.0 * np.apply_along_axis(lambda x: np.exp(-np.sum((point-x)**2.0))*(2.0*(point-x)),1,self.centers),0)
