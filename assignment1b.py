from math import *
def sumPrimes(n):
    sum = log (2)
    count = 0
    x = 1
    while ( count < n):
        x = x + 2
        i = 2
        while ( i < x):
            if ( x % i == 0):
                break
            elif ( i + 1 == x):
                count = count + 1
                sum = sum + log(x)
                print n, sum
                print n/sum
            i = i + 1
