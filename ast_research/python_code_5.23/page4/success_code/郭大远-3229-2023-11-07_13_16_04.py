list1=eval(input())
list2=list1.copy()
for x1 in list1:
    n=list1.count(x1)
    if n>1:
        while n>1:
            list2.remove(x1)
            n-=1
list2.sort()
print(list2)
    
