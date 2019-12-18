#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    
    arr = list(map(int, input().rstrip().split()))
    
    for i in range(0,n):
        x=n-i-1
        #print(x)
        print(arr[int(x)],end=" ")
    
    
