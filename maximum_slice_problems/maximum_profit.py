# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 00:09:03 2021

@author: Alberto Ciacci
"""
def maximum(a,b):
    if a >= b:
        return a 
    else:
        return b
    
def max_profit(X):
    n = len(X)
    max_profit = 0
    for i in range(n):
        for j in range(i,n):
            profit = (X[j] - X[i])
            if profit > max_profit:
                max_profit = profit
    return max_profit

def max_profit_linear(X):
    max_ending = max_slice = 0
    for x in X:
        max_ending = maximum(0, max_ending + x)
        max_slice = maximum(max_slice, max_ending)
    return max_slice
