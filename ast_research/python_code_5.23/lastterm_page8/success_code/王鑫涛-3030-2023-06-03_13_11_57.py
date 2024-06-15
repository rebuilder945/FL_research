name=input().split(',')
a=input().split(',')
for s in a:
    s=eval(s)
b={}
for i in range(len(a)):
    b[name[i]]=a[i]
a.sort()
if a[0]>a[1]:
    print('error')
d=[]
for r in a:
    for o in b:
        if b[o]==r:
            d.append([o,eval(b[o])])
print(d)
