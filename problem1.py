#!/usr/bin/env python
# coding: utf-8

def ismultiple(n,m):
    if n % m == 0:
        return True
    else:
        return False

x = 0 
for i in range (1000):
    if ismultiple(i,3) or ismultiple(i,5):
        x = x +i
        
print( 'The sum of all multiple of 3 and 5 between 1 and 100 is {}'.format(x))
# answer is 233168
##