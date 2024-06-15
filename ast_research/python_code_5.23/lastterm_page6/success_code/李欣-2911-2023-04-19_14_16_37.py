a=str(int(input()))
b=list(a)
c=[]
for x in b:
    m=str(int(x)+5)
    c.append(m)
c=reversed(c)
d=int(''.join(map(str,c)))
print(d)
