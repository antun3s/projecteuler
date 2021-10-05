#!/usr/bin/env python
# coding: utf-8

def check_palindromic(x):
    x = list( map(int, str(x) ) )
    if x == x[::-1]:
        return True
    else:
        return False

biggest_palindromic = 0

for i in range(999,99,-1):
    for j in range(999,99,-1):
        result = i * j
        if check_palindromic( result ):
            if biggest_palindromic < result:
                biggest_palindromic = result

print (biggest_palindromic)