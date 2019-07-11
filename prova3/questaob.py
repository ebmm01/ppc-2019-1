n = list(map(int, input().split()))
estudantes = []
outp = []
ss = []
x = 0
for i in range(n[0]):
    estudantes.append(list(map(int, input().split())))
    estudantes[i].append(i+1)

estudantes = sorted(estudantes)[::-1]

for i in range(10):
    try:
        outp.append(estudantes[i])
    except IndexError:
        break
    
sublists = []

for i, item in enumerate(outp):
    try:
        print(outp.count(outp[i][0]), outp[i][0])
        if outp.count(outp[i]) == 1:
            
            ss.append(outp[i][2])
            outp.pop()
        else:
            sublists = outp[0::outp.count(outp[i])]
            print(sublists, "sdwdasd")
            sublists = sublists[::-1]
            for value in sublists:
                outp.pop()
                ss.append(value[2])
    except IndexError:
        break


print(ss)
