list1=eval(input())
list2=list1.copy()
for x1 in list1:
    a=list2.count(x1)
    for i in range(a-1):
        list2.remove(x1)
print(list2)
            

