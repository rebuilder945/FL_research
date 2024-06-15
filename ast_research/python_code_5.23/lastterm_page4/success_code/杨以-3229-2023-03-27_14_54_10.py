list1 = eval(input())
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
if list2 == []:
    print("False")
else:
    list2.sort()
    print(*list2,sep=',')

