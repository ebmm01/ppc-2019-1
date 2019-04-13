n = int(input())
data = []
for i in range(n):
    data += list(map(int, input().split()))

print(data)
x = 0
for i in range(int(len(data)-2)):
    print(i)
    if i%2 == 0 or i==0:
        x += int(data[i] + data[i+1])
    else:
        x += int(data[i]-data[i+1])

print(x)
