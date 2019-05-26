from math import ceil

lst = list(map(int, input().split()))
outlst = []

if lst[1] <= ceil(lst[0]/2):
    print(2*lst[1] - 1)
else:
    print(2*(lst[1]-ceil(lst[0]/2)))
