
strength = list(map(int, input().split()))
# str = strength[0]
enemy = []
indexlst = 0
counter = 0
for i in range(strength[1]):
    enemy.append(tuple(map(int, input().split())))
    
for i in range(len(enemy)):
    indexlst= enemy.index(min(enemy))
    if strength[0] > enemy[indexlst][0]:
        strength[0] += enemy[indexlst][1]
        del enemy[indexlst]
        index = 0
    else:
        counter +=1
        break
    
if counter:
    print("NO")
else:
    print("YES")
