a=input()
c=[]
for i in range(len(a)):
    if i<(len(a)-1) and a[i].isalpha() and a[i+1].isdigit():
        c.append(a[i])
    if a[i].isdigit():
        c.append(a[i])
for i in range(len(c)):
    if c[i].isalpha():
        c[i]='*'
d=''.join(str(i) for i in c)
e=d.split('*')
g=[]
for i in e:
    f=len(i)
    g.append(f)
g.reverse()
h=g.index(max(g))
print(e[h])
        
