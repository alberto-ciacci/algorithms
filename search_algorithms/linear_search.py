# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 02:47:48 2021

@author: Alberto Ciacci
"""
import numpy as np

def linear_search(X, guess):
    
    for i in range(0, len(X), 1):
        if X[i] == guess:
            return i
    return -1
    
    
if __name__ == "__main__":
    
    n = int(input("Input the size of the random and uniformly distributed vector (integer) that we are about to create: "))
    low = int(input("Input the lower bound of the uniform distribution: "))
    high = int(input("Input the upper bound of the uniform distribution: "))
    X = np.random.randint(low,high,n)
    guess = int(input("Guess an integer: "))
    guess_idx = linear_search(X, guess)
    if guess_idx == -1:
        print('\nSorry, your guess is not an element of the random vector.')
    else:
        print('\nYour guess is the {0}-th element of the random vector'.format(guess_idx + 1))
    print("\nHere the random vector:")
    print(X)