list1 = eval(input())
list2 = []
for x in list1:
    if list1.count(x) == 1:
        list2.append(x)
if len(list2) == 0:
    print("False")
else:
    list2.sort()
    s = ''
    for i in list2:
        s += str(i) + ','
    print(s[0:-1])   
