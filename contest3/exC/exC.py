n = int(input())
lst = []
x = 0
for i in range(n):
    lst = list(map(int, input().split()))
    if sum(lst) >= 2:
        x += 1
    lst = []
    
print(x)
