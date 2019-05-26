n = list(map(int, input().split()))

trestante = 240 - n[1]
result = 0
i = 0
for j in range(1, n[0]+1):
    result += j*5
    i+=1
    if result > trestante:
        i -= 1
        break
    
print(i)
