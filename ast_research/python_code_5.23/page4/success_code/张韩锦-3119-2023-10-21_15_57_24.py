lst=eval(input())
lst2=lst.copy()
for i in lst:
    if lst.count(i)>=1:
        lst2.remove(i)
print(lst2)
