#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = []

    for i in range(4):
        for j in range(4):
            sum=0
            for k in arr[i][j:j+3]:
                sum+=k
            sum+=arr[i+1][j+1]
            for k in arr[i+2][j:j+3]:
                sum+=k
            result.append(sum)


    result.sort()
    print(result[len(result)-1])
    
