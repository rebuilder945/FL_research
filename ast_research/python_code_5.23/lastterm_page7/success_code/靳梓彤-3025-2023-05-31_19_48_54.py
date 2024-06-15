dic={}
ls=input().split()
lst=[]
for i in ls:
    dic[i]=ls.count(i)
for x in dic:
    h=dic[i]
    key=1
    for m in dic:
        if dic[m]>h:
            key=1
            break
    if key==0:
        lst.append(x)
lst.sort()
for p in lst:
    print(p,end="")
    print(ls.count(p))
