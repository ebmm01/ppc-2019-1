valor_emprestimo = list(map(int, input().split()))
eventos = list(map(int, input().split()))

n = 0
valor_pego = 0
total = 0
for i in range(len(eventos)):
    total += eventos[i]
    if total < 0:
        valor_pego += abs(total)
        total = 0

if valor_pego > valor_emprestimo[0]:
    print("-1")
else:
    print(valor_pego)
