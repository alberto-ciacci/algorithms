# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:37:26 2021

@author: Alberto Ciacci
"""
import math
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

def find_unique(X):
    random_quick_sort(X, 0, len(X) - 1)
    last_term = None
    unique_X = []
    for el in X:
        if last_term != el:
           unique_X.append(el)
        last_term = el
    return unique_X


def is_prime(n):
    if n > 1:
        if n == 2: 
            return True
        for i in range(2,n,1):
            if n % i == 0:
                return False
        return True
    return False

def prime_divisors(n):
    # write your code in Python 3.6
    p_divs = []
    i = 1
    while i <=math.sqrt(n):
        if (n%i == 0):
            if is_prime(i):
               p_divs.append(i)
            if is_prime(int(n/i)):
               p_divs.append(int(n/i))
        i+=1
    return(find_unique(p_divs))

def is_semiprime(n):
    # write your code in Python 3.6
    i = 1
    while i <=math.sqrt(n):
        if (n%i == 0):
            if (is_prime(i)) & (is_prime(int(n/i))):
               return True                 
        i+=1
    return False
