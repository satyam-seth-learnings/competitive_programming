#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    l=[]
    s1,s2=0,0
    for i in range(3):
        if a[i]>b[i]:
            s1+=1
        elif a[i]<b[i]:
            s2+=1
        else:
            pass
    l.insert(0,s1)
    l.insert(1,s2)
    return l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
