# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 23:44:03 2021

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

def perimeters(n):
    # write your code in Python 3.6
    i = 1
    p = []
    while i <=math.sqrt(n):
        if (n%i == 0):
            if(n/i == i):
                p.append(4*i)
            else:
                p.append(2*(i + n/float(i)))
        i+=1
    return(p)

if __name__ == "__main__":
    
    n = int(input("What is the area of the rectangle: "))
    ps = perimeters(n)
    random_quick_sort(ps,0,len(ps)-1)
    print("\nThe smallest perimiter of a rectangle of such area is: {0}:".format(ps[0]))