# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 13:40:00 2021

@author: Alberto Ciacci
"""
import numpy as np
import sys

def merge(X, a, n, b):
	
    n1 = n - a + 1
    n2 = b - n
    L1 = [0]*(n1 + 1)
    L2 = [0]*(n2 + 1)
    for i in range(n1):
        L1[i] = X[a + i]
    for i in range(n2):
        L2[i] = X[n + i + 1]
	
    L1[-1] = sys.maxsize
    L2[-1] = sys.maxsize
    counter1 = 0
    counter2 = 0
    
    for i in range(a, b+1, 1):
        if L1[counter1] <= L2[counter2]:
            X[i] = L1[counter1]
            counter1 +=1
        else:
            X[i] = L2[counter2]
            counter2 +=1


def merge_sort(X, a, b):
	if (a < b):
		mid = int(np.floor(0.5*(a+b)))
		merge_sort(X, a, mid)
		merge_sort(X, mid + 1, b)
		merge(X,a,mid,b)


if __name__ == "__main__":
    
    n = int(input("Input the size of the random and uniformly distributed vector (integer) that we are about to create and sort: "))
    low = int(input("Input the lower bound of the uniform distribution: "))
    high = int(input("Input the upper bound of the uniform distribution: "))
    X = np.random.randint(low,high,n)
    merge_sort(X, 0, len(X) - 1)
    print("\nHere the sorted random vector:")
    print(X)