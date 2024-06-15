a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
b.sort()
if len(b)==0:
    print("False")
else:
    c=[]
    for x in b:
        c.append(str(x))
    d=",".join(c)
    print(d)


