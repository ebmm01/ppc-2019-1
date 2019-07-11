n = int(input())
salarios = list(map(int, input().split()))
n_questoes = int(input())
faixas = []
output_lst = [ 0 for i in range(n_questoes)]
a = b= 0

for i in range(n_questoes):
    faixas.append(list(map(int, input().split())))
    a = faixas[i][0]
    b = faixas[i][1]
    
    for index,item in enumerate(salarios):
        if a <= item <= b:
            output_lst[i] +=1
            
for item in output_lst:
    print(item)
