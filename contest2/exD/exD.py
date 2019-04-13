x = int(input())
lst = list(map(int, input().split ()))
ind = 0

print([i for i, x in enumerate(lst) if x == min(lst)])
while lst[0] is not max(lst):
    maxvalue = lst.index(max(lst))
    lst[maxvalue-1], lst[maxvalue] = lst[maxvalue], lst[maxvalue-1]
    ind = ind+1

while lst[-1] is not min(lst):
    minvalue = max([i for i, x in enumerate(lst) if x == min(lst)])
    lst[minvalue], lst[minvalue+1] = lst[minvalue+1], lst[minvalue]
    ind = ind+1    
    

print(ind)
