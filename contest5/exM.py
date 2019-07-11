header = input()
msg = input()

header.replace(" ", "")
msg.replace(" ", "")

header = ''.join(sorted(set(header.lower())))
msg = ''.join(sorted(set(msg.lower())))

x = 0

for elem in msg:
    if not elem in header:
        x += 1
print(msg, header)
if x > 0:
    print("NO")
else:
    print("YES")
