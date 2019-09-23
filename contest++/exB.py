inp = list(map(int, input().split()))
caixas = list(map(int, input().split()))
n = 0
lst = []
atual = 0

lst.append(caixas.pop(0))

for index,item in enumerate(caixas):
    if len(lst) == (inp[1]) :
        break
    elif item > lst[-1]:
        pass
    else:
        lst.append(item)

print(sum(lst))    
