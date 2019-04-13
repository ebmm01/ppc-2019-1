st = input()
c1 = 0
c2 = 0

for i in st:
    if i.islower():
        c1 = c1 +1
    else:
        c2 = c2+1

if c1 >= c2:
    st = st.lower()
else:
    st = st.upper()
    
print(st)
