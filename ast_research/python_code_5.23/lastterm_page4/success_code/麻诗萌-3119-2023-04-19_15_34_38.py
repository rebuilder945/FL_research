lst=eval(input())
lst1=lst[:]
for x in lst:
    if lst.count(x)>1:
        lst1.remove(x)
print(lst1)

