list1=str(input())
if list1.count(i for i in list1)==1:
    pass
elif list1.count(i for i in list1)>1:
    while list1.count(i for i in list1)==1:
        list1.remove(i for i in list1)
        break
print(list1)
