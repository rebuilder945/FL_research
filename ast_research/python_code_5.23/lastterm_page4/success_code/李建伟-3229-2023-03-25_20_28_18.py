lst = eval(input())
lst1 = []
for i in lst:
    n = lst.count(i)
    if n == 1:
        lst1.append(i)
        lst1.sort()
if lst1 == []:
    print("False")
else:
    print((",".join(str(x) for x in lst1)))
