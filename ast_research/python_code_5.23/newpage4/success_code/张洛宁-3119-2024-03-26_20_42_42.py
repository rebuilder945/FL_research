list1=eval(input())
for x in list1[:]:
    if list1.count(x)>1:
        list1.remove(x)
print(list1)
