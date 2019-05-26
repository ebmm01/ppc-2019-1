import string

alf = list(string.ascii_lowercase)

n = int(input())

str = input()
 
str = set(list(str.lower()))

str = list(str)

str.sort()

if str == alf:
    print("YES")
else:
    print("NO")

