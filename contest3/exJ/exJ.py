from math import sqrt

lst = list(map(int, input().split()))

a = sqrt((lst[2]*lst[0])/lst[1])
b = lst[0]/a
c = (lst[1]/lst[0])*a

print(int(4*a + 4*b + 4*c))
