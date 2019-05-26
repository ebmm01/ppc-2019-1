from math import ceil

lst = list(map(int, input().split()))
outlst = []

for i in range(1, ceil(lst[0]/2) +1):
    outlst.append(2*i -1)
        
for i in range(1, ceil(lst[0]/2) +1):
    outlst.append(2*i)
    
print(outlst[lst[1]-1])
