a=eval(input()) or "#"
l=[]
while a!="#":
    l.append(a)
    a=eval(input()) or "#"
n=len(l)
s=sum(l)
c=[]
c.append(n)
c.append(s)
print(*c)

















