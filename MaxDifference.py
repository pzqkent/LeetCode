#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def maxDifference(a):
    if a == []:
        return -1
    # if len(a) == 1:
    #     return -1
    difference = -1
    min_element = a[0]

    for i in range(1,len(a)):
        if (a[i] - min_element > difference):
            difference = a[i] - min_element
        if (a[i] < min_element):
            min_element = a[i]
    
    if difference == 0:
        return -1
    return difference
# def maxDifference(a):
#     n = len(a)
#     difference = -1
#     maxright = a[n-1]
#     for i in range(n-2,-1,-1):
#         if (a[i] > maxright):
#             maxright = a[i]
#         else:
#             diff = maxright - a[i]
#             if (diff > difference):
#                 difference = diff
#     if difference == 0:
#         return -1
#     return difference

    # Write your code here

if __name__ == '__main__':