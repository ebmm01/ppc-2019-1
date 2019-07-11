str = input()

if len(str) < 8:
    print("NO")
else:
    if str.count("0000000") > 0 or str.count("1111111") > 0:
        print("YES")
    else:
        print("NO")
