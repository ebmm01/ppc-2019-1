x1= list(input())
x2 = list(input())

x3 =  []

for i in range(len(x1)):
    if int(x1[i]) == int(x2[i]):
        x3.append('0')
    else:
        x3.append('1')

x3 = ''.join(x3)
print(x3)
