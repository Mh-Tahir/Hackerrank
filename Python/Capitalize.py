# Capitalize first letters
#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    #x = [word[0].upper() + word[1:] for word in s.split()]
    #return " ".join(x)
    l = list(s)
    for i in range(len(l)):
        if l[i - 1] == ' ' or i == 0:
            l[i] = l[i].upper()
    return ''.join(l)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
