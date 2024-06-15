list1=eval(input())
list2=list(set(x for x in list1 if list1.count(x)==1))
flag=len(list2)
if flag==0:
    print("False")
else:
    list2.sort()
    print(','.join(str(x)for x in list2))


