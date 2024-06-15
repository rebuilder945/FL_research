list1 = eval(input())
list2 = []
for i in range(list1):
    a = count(i)
    if a == 1:
        list2.append(i)
if len(list2) == 0:
    print("False")
else:
    print(list2)
