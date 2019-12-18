#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    result = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        matchobject = re.match(r'.*@gmail.com',emailID)

        if matchobject:
            result.append(firstName)
    
    result.sort()

    for i in result:
        print(i)
