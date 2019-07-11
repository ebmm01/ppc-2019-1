lst = list(map(int,input().split() ))
sum = esq = dire = 0

for i in range(1, lst[0]+1):
    dire = lst[0] - i
    
    if esq <= lst[2] and dire >= lst[1]:
        sum +=1
    
    esq +=1
    
print(sum)
