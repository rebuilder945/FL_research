str=eval(input())
lst=[]
for st in str:
    for i in st:
        lst.sppend(i)
ls=set(lst)
for x in ls:
    k=lst.count(x)
    print("%s,%d"%(x,k))
