lst=eval(input())
lst1=[]
lst2=[]
for i in lst:
    if lst.count(i)!=1:
        a=0
        lst1.append(a)
    else:
        a=1
        lst1.append(a)
b=sum(lst1)
if b>0:
    for i in lst:
        if lst.count(i)==1:
            lst2.append(i)
            lst3=sorted(lst2)
    print((',').join(str(x) for x in lst3))
else:
    print("False")
