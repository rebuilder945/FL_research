name=input().split(',')
a=input().split(',')
for s in a:
    s=eval(s)
b={}
for i in range(len(a)):
    b[name[i]]=a[i]
a.sort()
d=[]
for r in a:
    for o in b:
        if b[o]==r:
            d.append([o,b[o]])
print(d)
