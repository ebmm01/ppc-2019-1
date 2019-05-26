import itertools
n = int(input())
lst = list(map(int,  input().split()))
lst2 = []
n_5 = lst.count(5)
lst2 = list(itertools.product([0, 5], repeat=len(lst)))

lst2 = filter(lambda x: x.count(5) == n_5, lst2)
lst2 = list(lst2)
lst3 = []

print(lst2)
def toSTR(tup): 
    new_data = [''.join(w) for w in tup]
    print(list(new_data))
    sd =  ''.join(str(tup)) 
    return new_data

for i in range(len(lst2)):
    lst3.append(toSTR(lst2[i]))
    

print(lst3)

