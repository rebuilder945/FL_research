list1=eval(input())
list2=list1.copy()
for x in list1:
    n=list2.count(x)
    if n>1:
        while n>1:
            list2.remove(x)
            n-=1
print(list2)
