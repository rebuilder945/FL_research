a=input()
b=list(a)
c=[]
d=[]
e=[]
f=[]
for i in b:
    if i in "01234567889":
        e.append(i)
    elif i in "zxcvbnmasdfghjklpoiuytrewq":
        c.append(i)
    elif i ==" ":
        d.append(i)
    else:
        f.append(i)
print(len(c),len(d),len(e),len(f))

