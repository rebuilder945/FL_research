list = eval(input())
list1 = []
list2 = []
for i in list:
    if list.count(i)==1:
        list1.append(i)
    else:
        list2.append(i)
list1.sort()
if len(list2)==len(list):
    print(False)
else:
    print((",").join(str(i)for i in list1))

