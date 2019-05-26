n = int(input())
count = 0

for i in range(n):
    x = input()
    if '++' in x:
        count +=1
    else:
        count -= 1

print(count)
    
