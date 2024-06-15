list1=eval(input())
list2=list1.copy()
for i in list1:
    a=list2.count(i)
    while a>1:
        list2.remove(i)
        a-=1
print(list2)
