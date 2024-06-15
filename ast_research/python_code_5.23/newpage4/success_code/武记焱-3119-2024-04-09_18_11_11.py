list1=eval(input())
list2=[]
for i in list1:
    x=list1.index(i)
    if i in list1[x+1:]:
        list2.append(x)
    else:
        pass
list1.pop(x)
print(list1)
