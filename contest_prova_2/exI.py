str = input()

if str.isupper():
    print(str.swapcase())
elif str[0].islower() and str[1:].isupper():
    print(str.swapcase())
elif len(str) == 1:
    print(str.swapcase())
else:
    print(str)
