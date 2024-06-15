name=input().split(',')
a=input().split(',')
for s in a:
    s=eval(s)
b={}
for i in range(len(a)):
    b[name[i]]=a[i]
a.sort(reverse=True)
d=[]
for r in a:
    for o in b:
        if b[o]==r:
            d.append([o,r])
print(d)
