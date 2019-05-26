n = int(input())
lst = []
temp = ""
output_lst = []
for i in range(n):
    temp = input()
    if temp in lst:
        output_lst.append("YES")
    else:
        output_lst.append("NO")
    lst.append(temp)
    
for item in output_lst:
    print(item)
