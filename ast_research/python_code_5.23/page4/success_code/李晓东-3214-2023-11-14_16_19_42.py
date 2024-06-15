list1 = eval(input())
list2 = []
for x in list1:
    if x!=0:
        list2.append(x)
for i in list1:
    if i==0:
        list2.append(i)
print(list2)

