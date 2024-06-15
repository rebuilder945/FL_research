lst = [1,1,2,3]
lst1 = lst.copy()
for x in lst:
    if x==1:
        lst1.remove(x)
print(lst1)
