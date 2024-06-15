a=eval(input())
c=[]
for x in range(len(a)):
    if a.count(a[x])==1:
        c.append(a[x])
    if a.count(a[x])!=1:
        pass
if c==[]:
    print(False)
else:
    c.sort()
    s=""
    for x in range(len(c)-1):
        s=s+str(c[x])+","
    s+=str(c[-1])
    print(s)
