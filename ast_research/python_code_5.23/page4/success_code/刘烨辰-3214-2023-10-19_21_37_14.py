list1 = eval(input())
for x in list1:
    if x == 0:
        list1.remove(x)
        list1.append(0)
print(list1)
