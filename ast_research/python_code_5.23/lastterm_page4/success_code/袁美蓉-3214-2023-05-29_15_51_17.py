list1 = eval(input())
list2 =[]
list3 =[0]
for x in list1:
    if x != 0:
        list2.append(x)
a = list1.count(0)
list = list2+list3*a
print(list)



