#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    j=0
    spos=[]
    for i in s:
        if i.isspace():
            spos.append(s.index(i,j))
        j+=1
    sl=s.split()
    l1=list(map(lambda x: x.capitalize(),sl))
    l2=[]
    for i in "".join(l1):
        l2.append(i)
    for i in spos:
        l2.insert(i," ")
    return "".join(l2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
