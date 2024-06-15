list1=eval(input())
list2=[]
list3=[]
list4=[]
for i in list1:
    for m in list1:
        if i>m:
            list2.append(i)
for i in list1:
    if i not in list2:
        list3.append(i)
for i in list1:
    for m in list1:
        if i<m:
            list4.append(i)
for i in list1:
    if i not in list4:
        list3.append(i)
#TypeError: '>=' not supported between instances of 'int' and 'list'
for i in list3:
    while i in list1:
        list1.remove(i)
print(list1)



