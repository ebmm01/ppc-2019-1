n = int(input())
str = input()

if n%2 == 0:
    if str.count('A') < n/2:
        print("Danik")
    elif str.count('A') == n/2:
        print("Friendship")
    else:
        print("Anton")
else:
    if str.count('A') <= n//2:
        print("Danik")
    else:
        print("Anton")
