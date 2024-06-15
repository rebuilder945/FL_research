a=input()
yw="qwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM"
sz="0987654321"
o="1"
z=" "
q1=[]
w2=[]
e3=[]
r4=[]
for i in a:
    if i in yw:
        q1.append(o)
    elif i ==" ":
        w2.append(o)
    elif i in sz:
        e3.append(0)
    else:
        r4.append(o)
q11=str(len(q1))
w22=str(len(w2))
e33=str(len(e3))
r44=str(len(r4))
t=q11+z+w22+z+e33+z+r44
print(t)

