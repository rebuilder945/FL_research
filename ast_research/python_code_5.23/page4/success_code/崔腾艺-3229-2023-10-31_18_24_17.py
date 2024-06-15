a=eval(input())
c=[]
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
    print(c)
