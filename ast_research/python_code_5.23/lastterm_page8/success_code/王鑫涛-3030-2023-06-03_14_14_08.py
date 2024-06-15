name=input().split(',')
A=input().split(',')
a=[]
for s in A:
    a.append(int(s))
b={}
for i in range(len(a)):
    b[name[i]]=a[i]
a.sort()
d=[]
for r in a:
    for o in b:
        if b[o]==r:
            d.append([o,eval(b[o])])
print(d)

