a=eval(input())
c=[]
d=[]
for x in a:
    b=a.count(x)
    if b==1:
        c.append(x)
    else:
        pass
if c==[]:
    print(False)
else:
    c.sort()
    for i in c:
        e=str(i)
        d.append(e)
    f=",".join(d)
    print(f)
