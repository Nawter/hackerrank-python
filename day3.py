#!/bin/python

import sys


N = int(raw_input().strip())
if (N%2!=0) or (N%2==0 and N in xrange(6,21)): print "Weird"
if (N%2==0 and ((N in xrange(2,6)) or N>20)): print "Not Weird"