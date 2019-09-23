n = int(input())
lst = []
out_lst = []
x = ["a","e","i","o","u"]*2000

for i in range(n):
    lst.append(list(input()))
    

for item in lst:
    for index,subitem in enumerate(item):
        if subitem != " ":
            item +=x[0]
            #x.pop(0)
          
for item in lst:
    print(item)
