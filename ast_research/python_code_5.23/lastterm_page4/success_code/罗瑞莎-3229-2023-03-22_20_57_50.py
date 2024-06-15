lst = eval(input())
lst1 = []
for i in lst:
    if lst.count(i) == 1:
        lst1.append(i)
if lst1 == []:
    print("False")
else:
    lst1.sort()
    lst2 = list(map(str,lst1))
    lst3 = ','.join(lst2)
    print(lst3)
