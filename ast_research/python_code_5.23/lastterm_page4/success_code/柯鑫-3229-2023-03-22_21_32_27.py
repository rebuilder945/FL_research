list1=eval(input())
list2=[]
for x in list1:
    if list1.count(x)>1:
        pass
    else:
        list2.append(x)
if len(list2)==0:
    print("False")
elif len(list2)!=0:
    list2.sort()
    list3=",".join(str(i) for i in list2)
    print(list3)
