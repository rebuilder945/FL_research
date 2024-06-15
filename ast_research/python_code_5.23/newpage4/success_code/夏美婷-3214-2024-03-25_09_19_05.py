list1=eval(input())
list2=[]
for i in list1:
    if i==0:
        list2.append(i)
        list1.remove(i)
        print(list1)
for i in list1:
    if i==0:
        list2.append(i)
        list1.remove(i)
        print(list1)
list3=list1+list2
print(list3)        
