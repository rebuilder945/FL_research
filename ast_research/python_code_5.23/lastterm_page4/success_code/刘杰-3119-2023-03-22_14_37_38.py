list1=eval(input())
list2=list1.copy()
for x in list1:
    n=list2.count(x)
    while n>1:
        list2.remove(x)
print(list2)

