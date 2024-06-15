list=eval(input())
list1=reversed(list)
list0=[]
for i in list1:
    if i not in list0:
        list0.append(i)
list2=reversed(list0)
print(list2)
