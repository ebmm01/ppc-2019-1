lst = input()
lst = list(lst)

def convert(lst):
    matlist = []
    pluslist = []
    f_list = []
    for i in range(len(lst)):
        try:
            isinstance(int(lst[i]), int)
            matlist.append(lst[i])
        except ValueError:
            pluslist.append(lst[i])
    matlist = sorted(matlist)

    for i in range(len(matlist+pluslist)):
        while len(matlist) >1:
            f_list.append(matlist[0])
            matlist.pop(0)
            f_list.append(pluslist[0])
            pluslist.pop(0)
    f_list.append(matlist[0])
    return f_list

def retokenize(lst):
    return ''.join(lst)
x = convert(lst)

print(retokenize(x))
