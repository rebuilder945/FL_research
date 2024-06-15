a=input()
b=list(a)
c=[]
d=[]
e=[]
f=[]
for i in b:
    if i in "0123456789":
        e.append(i)
    elif i in "zxcvbnmasdfghjklpoiuytrewqASDFGHJKLZXCVBNMQWERTYUIOP":
        c.append(i)
    elif i ==" ":
        d.append(i)
    else:
        f.append(i)
print(len(c),len(d),len(e),len(f))

