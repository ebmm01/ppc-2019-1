n = int(input())

lst = list(map(int, input().split()))

minvalue = 9999
recon = []

for i in range(len(lst)):
    if i == len(lst)+1:
        pass
    try:
        if abs(lst[i] - lst[i+1]) < minvalue:
            minvalue = abs(lst[i] - lst[i+1])
            recon.append([i+1, i+2])
    except IndexError:
        if abs(lst[i] - lst[0]) < minvalue:
            minvalue = abs(lst[i] - lst[0])
            recon.append([i+1, 1])
            
recon = recon[-1]         

print(' '.join(map(str, recon)))
