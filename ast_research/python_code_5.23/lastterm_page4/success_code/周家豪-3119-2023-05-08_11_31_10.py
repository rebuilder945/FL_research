lst=eval(input())
lst2=lst.copy()
for x in lst:
    if lst2.count(x)!=1:
        lst2.remove(x)
print(lst2)
