# list1 = eval(input())
# a,b = eval(input())
# if a in list1 and b in list1:
#     for i in range(list1.index(b)-list1.index(a)):
#         list1.pop(list1.index(a)+1)
#     print(list1)
# else:
#     print("error")


list1 = eval(input())
a,b = eval(input())
list2 = []
if 0<=a<len(list1-1) and 0<=b<len(list1-1) and a<=b:
    for i in range(len(list1)):
        if a==b:
            if list1[i]!=a:
                list2.append(list1[i])
        else:
            if list1[i] <= a or list1[i] > b:
                list2.append(list1[i])
    print(list2)
else:
    print("error")
