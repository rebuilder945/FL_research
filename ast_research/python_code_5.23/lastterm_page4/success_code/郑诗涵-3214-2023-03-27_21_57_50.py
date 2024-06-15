lst = eval(input())
m = lst.count(0)
lst1 = []
for i in lst:
    if i!=0:
        lst1.append(i)
for x in range(m):
    lst1.append(0)
print(lst1)
