a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0

for i in range(1,e+1):
    flag = 0
    if i%a == 0 and not flag:
        flag = 1
        count +=1
    elif i%b == 0 and not flag:
        flag = 1
        count +=1
    elif i%c == 0 and not flag:
        flag = 1
        count +=1
    elif i%d == 0 and not flag:
        flag = 1
        count +=1

print(count)
