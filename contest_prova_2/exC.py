import re
n = int(input())
str = input()

lst = list(str)

print(len(re.findall(r'(?=(xxx))', str)))
