str = input()
x=0
str2 = str
def checkrepeat(i,str, n=0):
    for elem in str:
        if elem == i:
            n+=1
    return n-1 if n>0 else  0

for i in str:
    x += checkrepeat(i,str)
    str = str.replace(i, "")

if not (len(str2) - x)%2:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
