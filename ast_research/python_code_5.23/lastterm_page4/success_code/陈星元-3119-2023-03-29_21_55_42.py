list=eval(input())
list2=list[:]
for x in list:
    while list2.count(x)>=2:
        list2.remove(x)
print(list2)
