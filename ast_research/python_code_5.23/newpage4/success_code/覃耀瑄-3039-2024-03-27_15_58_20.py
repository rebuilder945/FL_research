list1=input()
list1.sort()
for x in list1[0]:
    while x in list1:
        list1.remove(x)
for m in list1[-1]:
    while m in list1:
        list1.remove(m)
        print(list1)

