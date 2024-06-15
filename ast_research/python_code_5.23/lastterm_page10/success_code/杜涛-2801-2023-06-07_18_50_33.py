s=input()
q=0
a=[]
b=[]
c=[]
d=[]
for i in s:
    if i.isdigit():
        a.append(i)
    elif 'A'<=i<='Z':
        b.append(i)
    elif 'a'<=i<='z':
        c.append(i)
    else:
        d.append(i)
for i in [a,b,c,d]:
    if i!=[]:
        q+=1
if len(s)>=8:
    q+=1
print(q)

    

