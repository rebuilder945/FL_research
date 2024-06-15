lst=eval(input())
lst1=lst.copy()
for i in lst:
    while lst1.count(i)>1:
        lst1.remove(i)
print(lst1)
