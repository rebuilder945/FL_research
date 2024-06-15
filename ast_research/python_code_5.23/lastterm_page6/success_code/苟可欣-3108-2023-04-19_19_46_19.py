str=eval(input())
lst=[]
for st in str:
    for i in st:
        lst.append(i)
ls=set(lst)
ls1=list(ls)
ls1.sort()
for x in ls1:
    k=lst.count(x)
    print("%s,%d"%(x,k))
