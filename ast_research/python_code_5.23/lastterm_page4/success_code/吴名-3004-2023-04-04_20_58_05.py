lst=eval(input())
n=list(range(2,1000,1))
m=[]
l=[]
for i in lst:
    for x in n:
        y=i/x
        if y in n:
            m.append(i)
for a in lst:
    if a not in m:
        l.append(a)
if 0 in l:
    l.remove(0)
if 1 in l:
    l.remove(1)
print(l)
