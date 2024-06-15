a=list(input())
c=0
d=[]
l=0
u=[]
l=len(a)
s=[]
for i in a:
    if i.isdigit():
        d.append(i)
    elif i.islower():
        l+=1
    elif i.isupper():
        u.append(i)
    elif i in "~!@#$%^&*()_=-/,.?<>;:[]{}|":
        s.append(i)
if len(d)!=0:
    c+=1
if l!=0:
    c+=1
if len(u)!=0:
    c+=1
if l>=8:
    c+=1
if len(s)!=0:
    c+=1
print(c)



            

