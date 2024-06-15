a,b,c,d=input().split()
b,c,d=int(b),int(c),int(d)
stu=dict(name=a,english=b,python=c,math=d)
avge="%.2f"%((b+c+d)/3)
stu["avg"]=avge
e=[]
for k,v in stu.items():
    e.append([k,v])
f=[]
for x in range(len(e)):
    f.append(e[x][1])
i=[]
g=f[0]
for x in f[1:-1]:
    i.append(x)
i.sort(reverse=True)
h=[]
for x in i:
    x='%.2f'%(x)
    h.append(x)
h.append(avge)
h.insert(0,g)
for x in h:
    print(x,end=' ')



