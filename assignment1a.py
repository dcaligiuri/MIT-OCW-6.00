def thousandthPrime():
    count = 0
    x = 1
    while ( count < 999):
        x = x + 2
        i = 2
        while ( i < x):
            if ( x % i == 0):
                break
            elif ( i + 1 == x):
                count = count + 1
            i = i + 1
        if count == 999:
            print x
    
