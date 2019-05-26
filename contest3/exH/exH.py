ncoordinates = int(input())
coordinates = []
n = 0
for i in range(ncoordinates):
    coordinates.append(tuple(int(n) for n in input().split(' ')))

def check_neighbor(coordinates, item, i):
    temp = coordinates.copy()
    temp.pop(i)
    direito = 0
    esquerdo = 0
    topo = 0
    baixo = 0
    x = 0
    
    for i in range(len(temp)):
        # vizinho direito
        if item[0] > temp[i][0] and item[1] == temp[i][1]:
            direito +=1
        if item[0] < temp[i][0] and item[1] == temp[i][1]:
            esquerdo +=1 
        if item[0] == temp[i][0] and item[1] < temp[i][1]:
            baixo +=1
        if item[0] == temp[i][0] and item[1] > temp[i][1]:
            topo +=1
    if topo >0 and baixo > 0 and direito > 0 and esquerdo >0:
        x += 1
    temp = []
    return x

for i in range(len(coordinates)):
    n += check_neighbor(coordinates, coordinates[i], i)
    
print(n)
