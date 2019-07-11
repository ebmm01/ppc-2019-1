n = int(input())
lst = []
for i in range(n):
    lst.append(input())
    
teams = list(set(lst))

if len(teams) > 1:
    if lst.count(teams[0]) > lst.count(teams[1]):
        print(teams[0])
    else:
        print(teams[1])
else:
    print(teams[0])
