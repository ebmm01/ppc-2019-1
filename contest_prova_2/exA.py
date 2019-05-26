x = input()
 
if x.count('a') > len(x)/2:
    print(len(x))    
else:
    print(int(2*(x.count('a'))-1))
