# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:03:10 2021

@author: Alberto Ciacci
"""
import math
def fibonacci_binet(n):
    return int(((1 + math.sqrt(5.0))**n - (1 - math.sqrt(5.0))**n)/((2**n)*math.sqrt(5)))

A = [0,0,0,1,1,0,1,0,0,0,0]
n = len(A)
F = []
k = 0
pos = -1
n_jumps = 0
current = 0
previous = 0
while current + previous <= n:
    previous = current
    current = fibonacci_binet(k)
    F.append(current)
    k += 1
F = F[::-1]
for i in range(len(F)):
    jump_size = F[i] + pos 
    if A[jump_size] == 1:
       pos += F[i]
       n_jumps += 1
