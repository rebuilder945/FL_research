lst=eval(input())
c=[]
for x in lst:
    for i in x:
        c.append(i)
for ans in c:
    sums=c.count(ans)
    print(ans,sums)
