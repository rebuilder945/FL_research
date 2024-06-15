list1 = eval(input())
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.insert(0,i)
list2.sort()
if len(list2) == 0:
    print(False)
else:
    list3 = [str(x) for x in list2]
    a = ",".join(list3)
    print(a)

    

