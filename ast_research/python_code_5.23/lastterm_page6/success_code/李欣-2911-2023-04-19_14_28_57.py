a=str(int(input()))
b=list(a)
c=[]
for x in b:
    m=str((int(x)+5)%10)
    c.append(m)
c=reversed(c)
z=len(c)
d=int(''.join(map(str,c)))
d=str(d).zfill(z)
print(d)
