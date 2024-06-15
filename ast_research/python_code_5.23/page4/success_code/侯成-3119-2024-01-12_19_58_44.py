list1=eval(input())
for x in list1:
    a=list1.count(x)
    if a>1:
        list1.remove(x)
print(list1)
