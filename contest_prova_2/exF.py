import string

prev = 'a'
next = ''
ab = dict(zip(string.ascii_lowercase, range(1,27)))

n = input()
result = 0
lst = list(n)


for i in range(len(lst)):
    next = lst[i]
    if abs(ab[next] - ab[prev]) >= 13:
        result += (26- max(ab[next],ab[prev])) + min(ab[prev], ab[next])
    else:
        result += abs(ab[next] - ab[prev])
    prev = lst[i]
    
print(result)
