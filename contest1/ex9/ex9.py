n = int(input())
row = input()
row = list(row)

c = 0

for i in range(len(row)):
    if  i + 1 < len(row) and row[i] == row[i+1]:
        c = c+1
        
print(c)        
