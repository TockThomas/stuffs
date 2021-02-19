#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

if 0 != N % 2:
    print("Weird")
elif 0 == N % 2:
    if N >= 2 and N <= 5:
        print("Not Weird")
    if N >= 6 and N <= 20:
        print("Weird")
    if N > 20:
        print("Not Weird")