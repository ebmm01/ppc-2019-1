cities = int(input())

lst = list(map(int, input().split()))
min_value = min(lst)
 
walk_to =  [i for i, x in enumerate(lst) if x == min_value]

if len(walk_to) > 1:
    print("Still Rozdil")
else:
    print(walk_to[0]+1)
