list1=eval(input())
list2=list1.copy()
for x in list1:
    n=list1.count(x)
    while n>1:
        list1.remove(x)
print(list1)
