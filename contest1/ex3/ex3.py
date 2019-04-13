s, t = map(int, input().split())
row = list(input())

for i in range(t):
    j =0
    while j < len(row):
        if j+1 < len(row) and row[j] == 'B' and row[j+1] == 'G':
            row[j], row[j+1] = row[j+1], row[j]
            j = j +1
        j = j + 1
            
print(''.join(row))
