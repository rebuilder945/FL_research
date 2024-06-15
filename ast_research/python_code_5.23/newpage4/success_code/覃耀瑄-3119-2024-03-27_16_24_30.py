list1=eval(input())
for i in list1:
    if list1.count(i)!=1:
        while i in list1:
            list1.remove(i)
print(list1)
