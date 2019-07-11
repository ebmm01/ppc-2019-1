n = int(input())
lst = []
output_lst = []
for i in range(n):
    lst.append(input())
    
for i in range(n):
    if lst[i] != "?":
        output_lst.append(lst[i].replace("+ ",""))
    if lst[i] == "?":
        try:
            print(output_lst[-1])
            output_lst.pop(-1)
        except IndexError:
            print("Backlog vazio")
