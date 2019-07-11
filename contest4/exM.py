str = input()

str = ''.join(char.lower() for char in str if char.lower() not in 'aeiou')


str = ''.join("."+char if char in "bcdfghjklmnpqrstvwxyz" else char for char in str)

print(str)
