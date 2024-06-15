lst=eval(input())
c=[]
d=[]
for x in lst:
    for i in x:
        c.append(i)
for x in c:
    if x not in d:
        d.append(x)
for ans in d:
    sums=c.count(ans)
    print(ans,sums)
