list1=eval(input())
list2=[]
list3=[]
for x in list1:
    if not list1.count(x)==1:
            continue
    list2.append(x)
for x in list2:
    if x not in list3:
        list3.append(x)
list3.sort()
if list3==[]:
    print(False)
else:
    print(','.join(str(x) for x in list3))

