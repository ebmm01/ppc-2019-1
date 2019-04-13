import math

def checkifprime(n):
    if n%2 == 0:
        return False
    else:
        for i in range(3, n):
            if n%i == 0:
                return False
    return True

x , y = list(map(int, input().split()))
z =0
if checkifprime(y) == False:
    print('NO')
else:
    for i in range(x+1, y):
        if checkifprime(i):
            z = 1+z
    if z >= 1:
        print('NO')
    else: 
        print('YES')

