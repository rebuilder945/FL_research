list1=eval(input())
list2=[]
list3=[]
for x in list1:
    for y in x:
        if y not in list2:
            list2.append(y)
list2.sort()
for x in list1:
    for y in x:
        list3.append(y)
for x in list2:
    a=list3.count(x)
    print(x,a,sep=",")
