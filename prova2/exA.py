teclas_def = int(input())

str_tec_def = input()

n_mensagens = int(input())
str = ""
msgs = []

for i in range(n_mensagens):
    str = input()
    msgs.append(str.lower())
    
lst_str_tec_def = [item for item in str_tec_def]

n = 0
for i in range(len(msgs)):
    for item in lst_str_tec_def:
        if item in msgs[i]:
            n+=1
        else:
            pass
            
    if n >= 1:
        print("Mensagem #%d: Carlos" % (i+1))
    else:
        print("Mensagem #%d: Beto ou Carlos" % (i+1))
    n = 0
