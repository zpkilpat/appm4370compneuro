# -*- coding: utf-8 -*-
"""
fibonacci.py

calculates the first `n' terms of the Fibonacci sequence
"""

# set n>=2: number of terms to print out
n = 3

# first two terms
n1, n2 = 1, 1
print(n1)
print(n2)
count = 2

# while loop to run 
while count < n:
    n3 = n1 + n2
    print(n3)
    # update values
    n1 = n2
    n2 = n3
    count += 1