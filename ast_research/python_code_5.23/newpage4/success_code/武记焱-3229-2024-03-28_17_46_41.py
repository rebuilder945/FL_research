list1=eval(input())
list2=[]
for x in list1:
    if list1.count(x)==1:
        list2.append(str(x))
    else:
        pass
if list2==[]:
    print("False")
else:
    list2.sort()
c=','.join(list2)
print(c)
