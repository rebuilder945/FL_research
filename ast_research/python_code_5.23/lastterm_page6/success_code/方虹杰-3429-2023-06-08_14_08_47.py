a=input()
b=list(a)
c=[]
d=[]
f=[]
g=[]
for i in b:
    if i==" ":
        d.append(i)
    elif '0'<=i<='9':
        f.append(i)
    elif 'a'<=i<='z' or 'A'<=i<='Z':
        c.append(i)
    else:
        g.append(i)
print(c,d,f,g)
print(len(c),len(d),len(f),len(g)) 
