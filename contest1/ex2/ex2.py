for i in range(5):
    matx = [inp for inp in map(int , input().split())]
    if sum(matx) > 0:
        x = i+1
        y = int(matx.index(1)+ 1)

result = abs(x- 3) +abs(y-3)
print(int(result))
