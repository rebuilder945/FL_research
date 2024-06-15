lst = eval(input())
lst2 = []
for x in lst:
    if lst.count(x)<=1:
        lst2.append(x)
    else:
        pass
lst2.sort()
lst3 = ','.join(str(i) for i in lst2)
print(lst3 or False)
