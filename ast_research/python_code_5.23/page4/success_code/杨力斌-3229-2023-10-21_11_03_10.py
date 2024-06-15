lst = eval(input())
lst2 = []
for i in lst:
    if lst.count(i) == 1:
        lst2.append(i)
lst2.sort()
if len(lst2) == 0:
    print("False")
else:
    strl = ",".join(map(str,lst2))
