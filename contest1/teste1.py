x_result = 0
y_result = 0 
z_result = 0

for i in range (int(input())):
    x,y, z = map(int, input().split())
    x_result = x_result + x
    y_result = y_result + y
    z_result = z_result + z

if not (x_result or y_result or z_result):
    print("YES")
else:
    print("NO")
 
