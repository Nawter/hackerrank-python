#!/bin/python

import sys
n = int(raw_input())
inp = map(int,raw_input().split(" "))
total = 0
def swap(x,y):
    temp = x
    x = y
    y = temp
    return (x,y)


for i in range(n):  
    swaps = 0
    for j in range(n-1):
        if inp[j] > inp[j+1]:
            inp[j],inp[j+1] = swap(inp[j],inp[j+1])
            swaps += 1
    if swaps == 0:
        break
    else:
        total += swaps
print "Array is sorted in %d swaps." % total
print "First Element: %d" % inp[0]
print "Last Element: %d" % inp[n-1]