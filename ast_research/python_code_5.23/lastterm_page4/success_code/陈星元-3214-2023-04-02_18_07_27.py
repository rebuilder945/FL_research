list=eval(input())
list2=[]
list3=[]
for x in list:
    if x !=0:
        list2.append(x)
    else:
        list3.append(x)
list4=list2+list3
print(list4)
