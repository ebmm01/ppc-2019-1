
data = list(map(int, input().split()))
toasts = []
drinks = data[1]*data[2]
toasts.append(int(drinks/data[0]))
toasts.append(data[3]*data[4])
toasts.append(int(data[5]/data[-1]))

print(int(min(toasts)/data[0]))
