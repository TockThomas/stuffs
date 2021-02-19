#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    x = 0
    y = 0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(6):
        arr2 = []
        arr2 = arr[i]
        if i <= 2:
            for j in range(6):
                x = x + arr2[j]
        else:
            for j in range(6):
                y = y + arr2[j]
                #print(arr2[j])
    if x > y:
        print(x)
    else:
        print(y)
