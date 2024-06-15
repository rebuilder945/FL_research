lst=eval(input())
lst1=lst.copy()
for i in lst1:
    if lst1.count(i)>1:
        lst.remove(i)
print(lst)
