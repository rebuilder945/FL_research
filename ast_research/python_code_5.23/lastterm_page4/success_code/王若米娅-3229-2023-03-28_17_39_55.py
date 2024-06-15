lst=eval(input())
lst2=[]
lst3=[]
for x in lst:
    a=lst.count(x)
    lst2.append(a)

if min(lst2)>1:
    print("False")
else:
    for i in lst:
        if lst.count(i)==1:
            lst3.append(i)
    lst3.sort()
    print(*lst3,sep=',')

