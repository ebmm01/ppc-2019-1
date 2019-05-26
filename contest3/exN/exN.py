x =float(input())

x2 = round(x/((1 + 5 ** 0.5) / 2))
x3 = round(x2/((1 + 5 ** 0.5) / 2))
x4 = round(x3/((1 + 5 ** 0.5) / 2))
x5 = round(x4/((1 + 5 ** 0.5) / 2))

if x == 3:
    print("1 1 1")
elif  x == 2:
    print("0 1 1")
elif x == 1:
    print("0 0 1")
else:
    print(x5, x4, x2)
