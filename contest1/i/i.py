row = input()
row = list(row)

c = 0

c2=0

for i in range(len(row)):
    if  row[i] == "4" or row[i] == "7":
        c = c+1

if c == len(row) or c%4==0 or c%7==0:
    print("YES")
else:
    print("NO")
