# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 21:19:42 2021

@author: Alberto Ciacci
"""
import numpy as np

def ropes(K,C):
    count = 0
    running_sum = 0
    for l in K:
        running_sum += l
        if running_sum >= C:
            count +=1 
            running_sum = 0
    return count

