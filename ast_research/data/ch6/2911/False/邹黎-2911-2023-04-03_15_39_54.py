a=input()
b=[]
c=[]
d=" "
for x in a:
    x=int(x)
    x+=5
    x=x%10
    b.append(x)
for x in reversed(b):
    c.append(str(x))
for x in c:
    d=d+x
d=int(d)
print(d)
