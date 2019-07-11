number = list(map(int, input().split() ) )
tvs = list(map(int, input().split() ) )
money = temp = 0
for i in range(len(tvs)):
    tvs[i] = tvs[i]*(-1)

tvs.sort(reverse = True)

for i in range(number[1]):
    temp = money
    money += tvs[i]
    if temp > money:
        money -= tvs[i]

if money >0 :
    print(money)
else:
    print(0)
