num=eval(input())
s="".join(i for i in num)
lst=[z for z in s]
sets=set(lst)
lists=[]
for x in sets:
    lists.append(x)
lists.sort()
for i in lists:
    a=lst.count(i)
    print(i,",",a,sep="")

