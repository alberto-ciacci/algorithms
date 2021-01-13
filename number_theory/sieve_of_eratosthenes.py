# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 02:44:32 2021

@author: Alberto Ciacci
"""
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
          if prime[p]:
             for i in range(p*p, n+1, p): 
                prime[i] = False 
          p+=1
    primes = []
    for i in range(2,n+1,1):
        if prime[i]:
           primes.append(i)
    return(primes)

if __name__ == "__main__":
    
    n = int(input("You want to find all the primes that are smaller than or equal to: "))
    primes = sieve_of_eratosthenes(n)
    print("\nHere the your primes:")
    print(primes)
          