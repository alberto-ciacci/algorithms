# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 02:28:51 2021

@author: Alberto Ciacci
"""
import math
def divisors(n):
    # write your code in Python 3.6
    ctr = 0
    i = 1
    while i <=math.sqrt(n):
        if (n%i == 0):
            if(n/i == i):
                ctr += 1
            else:
                ctr += 2
        i+=1
    return(ctr)

if __name__ == "__main__":
    
    n = int(input("You want to find all the divisors of: "))
    divs = divisors(n)
    print("\nHere the divisors of {0}:".format(n))
    print(divs)