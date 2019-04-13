n = int(input())

lst = [input() for i in range(n)]
out = []

def detokeninze(str):
    return str.split()

for i in range(n):
    if len(lst[i]) > 10:
        end = []
        end.append(lst[i][0])
        end.append(str(len(lst[i])-2))
        end.append(lst[i][-1])
        out.append(''.join(end))
    else:
        out.append(lst[i])
    
for i in range(n):
    print(''.join(detokeninze(out[i])))
