n = int(input())
list_n = list(map(int, input().split()))
min_n = 10001
max_n = 0
count = 0
for i in range(len(list_n)):
    if i == 0:
        min_n = list_n[i]
        max_n = list_n[i]
    else:
        if list_n[i] < min_n:
            min_n = list_n[i]
            count +=1
        elif list_n[i] > max_n:
            max_n = list_n[i]
            count +=1
print(count)
