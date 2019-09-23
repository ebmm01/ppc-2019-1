import math

n = int(input())

x = n**(1/3)

error_n = 0.00000001
if 1 - abs(math.trunc(x) - x) == 1:
    print(int(x))
elif 1 - abs(math.trunc(x) - x) > error_n:
    print(-1)
else:
    print(x.__round__())
