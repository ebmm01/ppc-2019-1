friends = int(input())
n = list(map(int, input().split()))
possibilities = 0

for i in range(sum(n), sum(n) + 5):
    if i%(friends+1):
        possibilities +=1
            
print(possibilities)
