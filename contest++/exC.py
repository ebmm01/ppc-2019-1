import math
dificuldade = float(input())
notas = list(map(float, input().split()))

notas = sorted(notas)
notas.pop(0)
notas.pop(-1)

media = math.fsum(notas)/5

final = media*dificuldade

print("%2.1f"%(final))
