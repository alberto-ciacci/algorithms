# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 02:56:37 2021

@author: Alberto Ciacci
"""
import numpy as np

def knapsack(capacity, values, weights):
    dp_table = np.zeros((capacity+1,len(weights)+1))
    for i in range(1,len(weights)+1,1):
        weight = weights[i-1]
        value = values[i-1]
        for j in range(1,capacity+1,1):
            dp_table[j,i] = dp_table[j,i-1]
            if (weight <= j):
                val = dp_table[j - weight, i-1] + value
                if (dp_table[j,i] < val):
                    dp_table[j,i] = val
                
    return dp_table[-1,-1]
        
    
if __name__ == "__main__":
    
    n = int(input("Input the number of different objects that can be added to the knapsack (integer): "))
    capacity = int(input("Input the capacity of the knapsack (integer): "))
    values   = np.zeros(n,dtype=int)
    weights  = np.zeros(n,dtype=int)
    for i in range(n):
        values[i] = int(input("Input the value of the {0}-th object: ".format(i+1)))
        weights[i] = int(input("Input the weight of the {0}-th object: ".format(i+1)))
    value = knapsack(capacity, values, weights)
    print("\nThe knapsack algorithm allowed us to collect a cumulative value of: {0}".format(value))
