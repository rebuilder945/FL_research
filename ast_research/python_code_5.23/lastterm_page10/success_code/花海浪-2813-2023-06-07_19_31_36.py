a=input()
b=input()
c=[]
d=[]
if b not in a:
    print(a)
else:
    for i in a:
        c.append(i)
    for i in b:
        d.append(i)
    for i in c:
        if i in d:
            c.remove(i)
    for i in c:
        print(i,end='') 
