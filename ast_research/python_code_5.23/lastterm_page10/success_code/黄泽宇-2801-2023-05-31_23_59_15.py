#x=input()
x='65102621'
x1=list(x)
a=0
r=[0]*4
if len(x1)>=8:
    a+=1

for i in x1:
        if i.isdigit():
            r[0]=1
        elif i.isupper():
            r[1]=1
        elif i.islower():
            r[2]=1
        else:
            r[3]=1
f=r.count(1)
d=a+f
print(d)


