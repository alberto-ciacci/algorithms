# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:53:34 2021

@author: Alberto Ciacci
"""
def GCD_euclid(a, b):
    if (b == 0):
        return a
    rem = a%b
    return GCD_euclid(b,rem)

if __name__ == "__main__":
    
    n1 = int(input("Input the first number: "))
    n2 = int(input("Input the second number: "))
    print("\nThe greatest common divisor between these two numbers is: {0}".format(GCD_euclid(n1,n2)))
      