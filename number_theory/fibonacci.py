# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 03:02:42 2021

@author: Alberto Ciacci
"""
import numpy as np

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_linear(n):
    f_0 = 0
    f_1 = 1
    for i in range(2,n+1,1):
        current = f_0 + f_1
        f_0 = f_1
        f_1 = current
    return f_1

def fibonacci_binet(n):
    return int(((1 + np.sqrt(5.0))**n - (1 - np.sqrt(5.0))**n)/((2**n)*np.sqrt(5)))

def closest_fibonacci(x):
    previous = 0
    current = 1
    while current < x:
        f_n = previous + current
        previous = current 
        current = f_n 
    d_1 = abs(x - current)
    d_2 = abs(x - previous)
    if d_1 <= d_2:
        return current
    else:
        return previous

if __name__ == "__main__":
    
    n = int(input("Input the index of the Fibonacci number you want to retrieve: "))
    print("The corresponding Fibonacci number is: {0}".format(fibonacci_binet(n)))