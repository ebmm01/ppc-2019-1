n = int(input())
lst = list(map(int, input().split()))

counter = 0
wd = 0

while counter < n:
    for i in range(len(lst)):
        if counter >= n:
            break
        else:
            counter += lst[i]
            wd +=1

if wd%7 == 0:
    print(wd)
else:
    print(wd%7)
