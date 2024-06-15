list1=eval(input())
for i in list1:
    a=list1.count(i)
    while a>1:
        list.remove(i)
        a-=1
print(list1)
