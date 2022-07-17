#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length=len(arr)
    n=z=p=0
    for i in arr:
        if i<0:
            n+=1
        elif i>0:
            p+=1
        else:
            z+=1
    print(f"{(p/length):.6f}")
    print(f"{(n/length):.6f}")
    print(f"{(z/length):.6f}")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
