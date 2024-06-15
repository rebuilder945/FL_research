list1 = eval(input())
for i in list1:
    if i == 0:
        list1.remove(i)
        list1.append(i)
print(list1)

