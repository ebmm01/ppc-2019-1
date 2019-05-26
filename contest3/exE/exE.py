elemtns = int(input())
array = list(map(int, input().split()))
elemtns1 = int(input())
search = list(map(int, input().split()))
vaysa = 0 #crescente
petya = 0 #decrescente
varlenarray = len(array)

dic= {}
for i in range(len(array)):
  dic[array[i]] = i+1
  
for i in search:
    var = int(dic.get(i))
    vaysa += var
    petya += int(varlenarray - var+1)

print(vaysa, petya)
