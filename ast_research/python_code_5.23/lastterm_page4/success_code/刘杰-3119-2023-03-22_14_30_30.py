list1=eval(input())
list2=list1.copy()
for x in list1:
    n=list1.count(x)
    if n>1:
        while n>1:
            list1.remove(x)
            n-=1
print(list1)
