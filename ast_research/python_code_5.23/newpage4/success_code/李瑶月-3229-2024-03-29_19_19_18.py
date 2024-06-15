list1 = eval(input())
list1 = []
list2 = []
for i in list1:
    if list1.count(i)==1:
        list1.append(i)
    else:
        list2.append(i)
list1.sort()
if len(list2)==len(list1):
    print(False)
else:
    print((",").join(str(i)for i in list1))

