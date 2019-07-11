n = int(input())
meses = soma = 0
lst = list(map(int, input().split() ))
lst.sort(reverse = True)

for i in range(len(lst)):
    soma += lst[i]
    meses += 1
    if soma >= n:
        break

if n == 0:
    print("0")
else:
    print(meses)
