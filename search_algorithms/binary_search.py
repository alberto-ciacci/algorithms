# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 01:39:07 2021

@author: Alberto Ciacci
"""
import numpy as np

def swap(X, a, b):
    
    tmp1 = X[a]
    tmp2 = X[b]
    X[a] = tmp2
    X[b] = tmp1

def random_partition(X, left, right):
    
    random_idx = np.random.randint(left, right)
    swap(X, left, random_idx)
    pivot = X[left]
    j = left
    for i in range(left+1,right+1,1):
        if X[i] <= pivot:
            j += 1
            swap(X, i, j)
            
    swap(X, j, left)
    return j

def random_quick_sort(X, left, right):
    
	if (left >= right):
		return
	idx = random_partition(X, left, right)
	random_quick_sort(X, left, idx-1)
	random_quick_sort(X, idx+1, right)


def binary_search(X, left, right, guess):
    
    if right <= left:
        return -1
    mid = int(np.floor(0.5*(left+right)))
    if guess == X[mid]:
        return mid
    elif guess < X[mid]:
        return binary_search(X, left, mid, guess)
    else:
        return binary_search(X, mid+1, right, guess)
    
    
if __name__ == "__main__":
    
    n = int(input("Input the size of the random and uniformly distributed vector (integer) that we are about to create: "))
    low = int(input("Input the lower bound of the uniform distribution: "))
    high = int(input("Input the upper bound of the uniform distribution: "))
    X = np.random.randint(low,high,n)
    random_quick_sort(X, 0, len(X) - 1)
    guess = int(input("Guess an integer: "))
    guess_idx = binary_search(X, 0, len(X), guess)
    if guess_idx == -1:
        print('\nSorry, your guess is not an element of the random vector.')
    else:
        print('\nYour guess is the {0}-th element of the random vector'.format(guess_idx + 1))
    print("\nHere the sorted random vector:")
    print(X)