n = list(map(int, input().split()))
rooms = list(map(int, input().split()))
room_number = list(map(int, input().split()))
i =  1
x=0
values = []
for room in rooms:
    values.append([i, room+i-1])
    i += room
    
for number in room_number:
    x = values[0][1]
    for j in range(len(values)):
        if values[j][0] <= number <= values[j][1]:
            print(j+1, number - values[j][0] +1)
        x += values[j][1]
    x = 0
