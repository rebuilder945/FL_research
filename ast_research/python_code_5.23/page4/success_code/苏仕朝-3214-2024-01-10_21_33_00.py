list1=eval(input())
list2=[]
for x in list1:
    x=int(x)
    if x==0:
        list2.append(x)
        list1.remove(x)
for x in list2:
    list1.append(x)
print(list1)

