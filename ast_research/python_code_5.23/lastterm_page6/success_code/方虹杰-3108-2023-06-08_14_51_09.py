a=eval(input())
b=[]
for i in range(len(a)):
    c=list(a[i])
    b+=c
f=[]
for i in b:
    t,y=i,b.count(i)
    f.append("%s,%d"%(t,y))
r=[]
for i in f:
    if i not in r:
        r.append(i)
r.sort()
for i in r:
    print(i)


    
