d = list(str(input()))
s=0
for i in range(len(d)):
    t = int(d[i])+5
    s+=t*(10**(i))
print(s)
