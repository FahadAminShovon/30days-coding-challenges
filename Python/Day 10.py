#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())    
    str = "";
    
    while(n>0):
        if(n%2==1):
            str="1"+str;
        else: 
            str = "0"+str;
        n//=2;
        
        
    sz = len(str)
    
    i = 0 ;
    l=[]
    
    while(i<sz):
        if(str[i]=="1"):
            counter = 1
            if(i!=sz-1):
                while(str[i+1]=="1"):
                    counter+=1
                    i+=1
                    if(i+1==sz):break

            l.append(counter)
        i+=1
        
    l.sort()

    print(l[len(l)-1])
    
