#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    for item in Counter(sorted(s)).most_common(3):
        print(*item)