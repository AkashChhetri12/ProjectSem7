# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:45:40 2019

@author: Me
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

temp = [1,2,3,4,5,6,7,8,9,0,1,1,1,2,3,2,1,3,1,4,2,1,12,3,1,12,1,23,12,2,1,1,2,0,12,0,31,4,1,2,1]

class DualSlidingWindow:
    def __init__(self, window_size, data, threshold):
        self.window_size = window_size
        self.data = data
        self.anchor = list()
        self.threshold = threshold
        self.data_len = len(data)
        
    def mahalonobis_distance(self, mean1, mean2, var1, var2):
        return ((mean1-mean2)**2)*((1/(2*var1))+(1/(2*var2)))
    
    def sliding_window(self):
        i= 0
        j= i + self.window_size
        k= j + self.window_size
        while k<len(self.data):
            try:
                w1 = self.data[i:j]
                w2 = self.data[j:k]
                mahalonobis_dis = self.mahalonobis_distance(np.mean(w1), np.mean(w2), np.var(w1), np.var(w2))
                print(w1,w2,mahalonobis_dis)
                if math.isinf(mahalonobis_dis):
                    i+=1
                    j+=1
                    k+=1
                elif math.isnan(mahalonobis_dis):
                    i+=1
                    j+=1
                    k+=1
                elif mahalonobis_dis > self.threshold:
                    self.anchor.append(j)
                    i+=self.window_size
                    j+=self.window_size
                    k+=self.window_size
                else:
                    i+=1
                    j+=1
                    k+=1
            except:
                print("except")
        print(self.anchor)
            
        
s = DualSlidingWindow(3, temp,15)
s.sliding_window()