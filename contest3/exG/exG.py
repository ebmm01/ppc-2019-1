nchild = list(map(int, input().split()))
childvalues = list(map(int, input().split()))

childvalues = list(enumerate(childvalues,1))
i = 0
while len(childvalues) > 1:
    if childvalues[0][1] <= nchild[1]:
        childvalues.pop(0)
    else:
        childvalues[0] = tuple([childvalues[0][0],childvalues[0][1] - nchild[1]])
        childvalues.append(childvalues[0])
        childvalues.pop(0)
    if len(childvalues) <= 1:
        break
    
print(childvalues[0][0])
