list1=eval(input())
list2=[]
list3=[]
for x in list1:
    if x==0:
        list2.append(x)
    else:
        list3.append(x)
list4=list3+list2
print(list4)

