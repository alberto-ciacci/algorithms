# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 21:49:03 2021

@author: Alberto Ciacci
"""
import random

def swap(X, a, b):
    
    tmp1 = X[a]
    tmp2 = X[b]
    X[a] = tmp2
    X[b] = tmp1
    
def random_partition_enhanced(X, left, right, shift):
    random_idx = random.randint(left, right)
    swap(X, left, random_idx)
    pivot = X[left]
    j = left
    for i in range(left+1,right+1,1):
        if(X[i] <= pivot):
            j +=1
            swap(X, j, i)
            if(X[j] == pivot):
                shift += 1
                swap(X, left + shift, j)
      	    
		
    for p in range(0, shift + 1, 1):
        swap(X, left + p, j - p)
    return j, shift


def random_quick_sort(X, left, right):
	if (left >= right):
		return
	
	shift = 0;
	idx, shift = random_partition_enhanced(X, left, right, shift)
	random_quick_sort(X, left, idx-1-shift)
	random_quick_sort(X, idx+1, right)



if __name__ == "__main__":
    
    n = int(input("Input the size of the random and uniformly distributed vector (integer) that we are about to create and sort: "))
    low = int(input("Input the lower bound of the uniform distribution: "))
    high = int(input("Input the upper bound of the uniform distribution: "))
    X = [random.randint(low,high) for i in range(n)]
    random_quick_sort(X, 0, len(X) - 1)
    print("\nHere the sorted random vector:")
    print(X)