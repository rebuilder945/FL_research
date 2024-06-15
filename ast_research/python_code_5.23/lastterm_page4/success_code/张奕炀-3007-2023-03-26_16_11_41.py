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
if a>min(list1) and b<max(list1):
    for i in range(len(list1)):
        if list1[i] <= a or list1[i] > b:
            list2.append(list1[i])
    print(list2)
else:
    print("error")
