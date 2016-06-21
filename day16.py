#!/bin/python

import sys

S = raw_input()
try:
    print(int(S))
except Exception as e:
    print('Bad String')