lst = list(input().split())

Fogo = {'Ar':'resistente', 'Terra':'imune', 'Agua':'vulneravel' }
Agua = {'Fogo':'resistente', 'Ar':'imune', 'Terra':'vulneravel' }
Ar = {'Terra':'resistente', 'Agua':'imune', 'Fogo':'vulneravel' }
Terra = {'Agua':'resistente', 'Fogo':'imune', 'Ar':'vulneravel' }

def receive(lst):
    if lst[1] == 'Fogo':
        calcula_dano(Fogo, lst)
    if lst[1] == 'Terra':
        calcula_dano(Terra, lst)
    if lst[1] == 'Ar':
        calcula_dano(Ar, lst)
    if lst[1] == 'Agua':
        calcula_dano(Agua, lst)
        
def calcula_dano(elem, lst, value=''):
    value = elem.get(lst[0])
    if value == 'resistente':
        print(int(int(lst[2])/2))
    if value == 'imune':
        print("0")
    if value == 'vulneravel':
        print(int(int(lst[2])*2))
    if value == None:
        print(lst[2])
        
receive(lst)
