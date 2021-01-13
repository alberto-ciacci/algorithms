# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 01:26:53 2021

@author: Alberto Ciacci
"""
import numpy as np

def fractional_knapsack(capacity, values, weights):
    
    picked_values  = np.zeros(n)
    picked_weights = np.zeros(n)
    for i in range(n):
        if capacity == 0:
           return picked_values, picked_weights
        best_score = 0
        best_idx = 0
        for j in range(n):
            if weights[j] > 0:
                current_score = values[j]/float(weights[j])
                if (current_score > best_score):
                    best_score = current_score
                    best_idx = j
        picked_weight = np.minimum(weights[best_idx],capacity)
        weights[best_idx] -= picked_weight
        capacity -= picked_weight
        picked_weights[best_idx] += picked_weight
        picked_values[best_idx] += picked_weight*best_score
    return picked_values, picked_weights
            

if __name__ == "__main__":
    
    n = int(input("Input the number of different objects that can be added to the knapsack (integer): "))
    capacity = int(input("Input the capacity of the knapsack (integer): "))
    values   = np.zeros(n)
    weights  = np.zeros(n)
    for i in range(n):
        values[i] = int(input("Input the value of the {0}-th object: ".format(i+1)))
        weights[i] = int(input("Input the weight of the {0}-th object: ".format(i+1)))
    picked_values, picked_weights = fractional_knapsack(capacity, values, weights)
    print("The fractional knapsack algorithm selected the following objects: ")
    for i in range(n):
        print("object: {0}, weight: {1}, value: {2}".format(i+1,picked_weights[i],picked_values[i]))
    print("The total value of the knapsack is: {0}".format(np.sum(picked_values)))