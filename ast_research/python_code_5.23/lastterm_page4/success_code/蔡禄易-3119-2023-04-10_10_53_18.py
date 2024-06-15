a = eval(input())
list1 = a.copy()
for i in a:
    if a.count(i) >= 2:
        list1.remove(i)
        list1.append(i)
print(list1)

