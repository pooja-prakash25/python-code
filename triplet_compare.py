import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice_score=0
    bob_score=0
    
    ret=[]
    for i in range(0,len(a)):
        if a[i]>b[i]:
            alice_score+=1
        elif a[i]<b[i]:
            bob_score+=1
        else :
            continue
        
    ret.append(alice_score)
    ret.append(bob_score)
    return ret
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(''.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
