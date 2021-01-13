# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:37:05 2021

@author: Alberto Ciacci
"""
import math

def max_non_overlapping(A, B):
    # write your code in Python 3.6
    end = -1
    cluster = 0
    n = len(A)
    if len(A) == 0:
       return 0
    for i in range(n):
        if (A[i] > end):
            cluster += 1
            end = B[i]
    return cluster