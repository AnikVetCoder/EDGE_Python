# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:33:08 2024

@author: Anik
"""

#Write a Python program that determines whether a given number is a prime number.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))

if is_prime(n):
    print("The given number is prime")
else:
    print("The given number is not prime")
