ls=input().split()
dic1={}
ls1=[]
for i in ls:
    dic1[i]=ls.count(i)
for x in dic1:
    h=dic1[x]
    key=0
    for m in dic1:
        if dic1[m]>h:
            key=1
            break
    if key==0:
        ls1.append(h)
ls1.sort()
for p in ls1:
    print(p,end=' ')
    print(ls.count(p))
