n_houses = list(map(int, input().split()))
houses = list(map(int, input().split()))

inicio = 1 
fim = 0
steps = 0

for i in range(len(houses)):
    fim = houses[i]
    if fim > inicio:
        steps += fim - inicio
    elif fim == inicio:
        pass
    else:
        steps += n_houses[0] - abs(inicio-fim)
    inicio = houses[i]
        
print(steps)
