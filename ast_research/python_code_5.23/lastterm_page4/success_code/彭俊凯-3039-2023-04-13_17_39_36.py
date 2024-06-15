a=eval(input())
b=min(a)
d=[]
e=[]
for i in range(len(a)):
    if a[i]!=b:
        d.append(a[i])
if d!=[]:
    c=max(d)
    for i in range(len(d)):
        if d[i]!=c:
            e.append(d[i])
    print(e)
else:
    print(d)
