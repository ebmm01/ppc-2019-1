size = list(map(int, input().split()))
chessboard_i = chessboard_o =  []
for i in range(size[0]):
    chessboard_i.append(list(input()))

for n in range(size[0]):
    for m in range(size[1]):
        if chessboard_i[n][m] == "-":
            pass
        elif n%2== 0:
            if m%2 != 0:
                chessboard_i[n][m] = "W"
            else:
                chessboard_i[n][m] = "B"
        else:
            if m%2 != 0:
                chessboard_i[n][m] = "B"
            else:
                chessboard_i[n][m] = "W"
    
for item in chessboard_i:
    print(''.join(item))
