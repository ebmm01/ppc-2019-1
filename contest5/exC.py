str = input()

hello = ['h','e','l','l','o']

str = str.lower()

str_lst = list(str)

while True:
    try:
        if str_lst[0] == hello[0]:
            str_lst.pop(0)
            hello.pop(0)
        else:
            str_lst.pop(0)
    except IndexError:
        break
if len(hello) == 0:
    print("YES")
else:
    print("NO")
