from math import factorial
lst = list(map(int, input().split()))
N = lst[0]
p = lst[1]
binomios = []
output_lst = []

for i in range(N+1):
    binomios.append(int(factorial(N)/(factorial(i)*(factorial(N-i)))))
    if binomios[i]%p == 0:
        output_lst.append("1")
    else:
        output_lst.append("0")
    
print("".join(output_lst))
