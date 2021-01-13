# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 23:50:19 2021

@author: Alberto Ciacci
"""

def maximum(a, b): 
      
    if a >= b: 
        return a 
    else: 
        return b 

def fibonacci_linear(n):
    f_0 = 0
    f_1 = 1
    F = [f_0, f_1]
    for i in range(2,n+1,1):
        current = f_0 + f_1
        f_0 = f_1
        f_1 = current
        F.append(current)
    return F

def n_combinations(n, F):
    return F[n] - F[maximum(n-1,0)]
    
    
if __name__ == "__main__":
    
    n = int(input("Input the number of ladders: "))
    F = fibonacci_linear(n)
    print("\nThere are {0} different ways to climb this stair.".format(n_combinations(n, F)))    