#!/usr/bin/env python
# coding: utf-8

def ismultiple(n,m):
    if n % m == 0:
        return True
    else:
        return False

b = 1
a = 2
max = 4000000
sum_even_numbers = 2


while a < max:
    aux = a
    a = a + b
    b = aux

    if a > max:
        break
    elif a % 2 == 0:
        sum_even_numbers = sum_even_numbers + a
    
    print(a)

print ('Sum of Fibonacci even numbers until 4,000,000 is {}'.format(sum_even_numbers))
# answer is 4613732 