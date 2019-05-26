import math, string

date = input()
x = 0
repeticoes = 0
n_char = 0
lst = [item for item in date]
lst_0 = [0 for item in range(0,10)]
hard_coded_dict = dict(zip(string.digits, lst_0))
for item in lst:
    if item == "/":
        lst.pop(lst.index(item))

for n in lst:
    hard_coded_dict[str(n)] += 1
    
for item in hard_coded_dict:
    x+= int(hard_coded_dict[item])
    if hard_coded_dict[item] > 1:
        n_char += 1

for i in range(1,10):
    if hard_coded_dict[str(i)] > 0:
        repeticoes += hard_coded_dict[str(i)]

print(int(720/math.factorial(6-repeticoes)))
