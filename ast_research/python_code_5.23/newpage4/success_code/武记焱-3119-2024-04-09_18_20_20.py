list1=eval(input())
list2=[]
for i in list1:
    x=list1.index(i)
    if i in list1[x+1:]:
        list2.append(x)
    else:
        pass
list3= [value for index, value in enumerate(list1) if index not in list2]
print(list3)
