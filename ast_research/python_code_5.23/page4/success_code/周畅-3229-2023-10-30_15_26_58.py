lst=eval(input())
lst2=[]
for x in lst:
    if lst.count(x)>1:
        for i in range (lst.count(x)):
            lst.remove(x)
if len(lst)>0:
    lst.sort()
    lst2=",".join(str(i) for i in lst)
    print(lst2)
else:
    print(False)
