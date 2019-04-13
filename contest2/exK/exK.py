lst = list(map(int, input().split()))
lst2= lst

def count_n(lst,x=0, atual=0, inc=0):
    if len(lst) == 0:
        return x
    atual = lst[0]
    for elem in range(1,len(lst)):
        if lst[elem] == atual:  
            x +=1
            lst.pop(0)
            inc = lst[0]
            return count_n(lst,x, inc=inc )
        if lst[elem] == inc:
            pass
                
    inc = lst.pop(0)
    
    return count_n(lst,x, inc=inc)

m = count_n(lst, inc=lst[0])            
print(m)
