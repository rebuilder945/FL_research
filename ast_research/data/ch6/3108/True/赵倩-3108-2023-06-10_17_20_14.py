a=eval(input())
l=[]
d=[]
e=[]
for i in a:
    c=list(i)
    l=l+c
l.sort()
for i in l:
    if i not in e:
        s=l.count(i)
        e.append(i)
        d.append([i,s])
for i in d:
    print(",".join(str(x) for x in i))























