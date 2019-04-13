lst = []
for i in range(4):
    lst += list(input().split())
x = 0    
def calcula_valor(str,n=0):
    vale_10 = ['T', 'Q', 'K', 'J']
    vale_1 = ['A', 'H','D','S','C']
    for i in str:
        try:
            n += int(i)
        except ValueError:
            if i in vale_10:
                n +=10
            if i in vale_1:
                n+=0
            
    return n

for i in range(len(lst)):
    x += calcula_valor(lst[i])
    if x >= 21:
        break
    
    

print(x)
