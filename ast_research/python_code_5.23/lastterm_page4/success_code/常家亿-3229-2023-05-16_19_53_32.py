lst = eval(input())
lst1 = []
for x in lst:
    if lst.count(x) == 1:
        lst1.append(x)
if len(lst1) == 0:
    print(False)
else:
    lst1.sort()
b = " "
for i in lst1:
    b += str(i) + ","
print(b)




