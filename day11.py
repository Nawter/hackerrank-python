#!/bin/python

import sys


import sys

arr = []
for i in xrange(6):
    arr.append(map(int, raw_input().strip().split()))
    
total = -sys.maxint-1
for i in xrange(1, 5):
    for j in xrange(1,5):
        partial = arr[i][j]+arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
        if partial > total:
            total = partial
print total