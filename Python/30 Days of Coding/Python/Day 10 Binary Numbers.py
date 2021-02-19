#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
n = bin(n).lstrip("0b")
x = 0
y = 0 
for i in range(len(str(n))): 
    if int(n[i]) == 1:
        x = x + 1
    if x > y:
        y = x
    if int(n[i]) != 1:
        x = 0 
print(y)
