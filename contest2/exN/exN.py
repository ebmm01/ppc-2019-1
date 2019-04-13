str_1 = input()
str_2 = input()
str_r = input()

str_3 = str_1 + str_2
str_3 = ''.join(sorted(str_3))
str_r = ''.join(sorted(str_r))

if (str_3) == (str_r):
    print('YES')
else:
    print('NO')
