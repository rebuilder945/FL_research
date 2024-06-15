lst=eval(input())
lst.sort()
lst1=lst.copy()
maxl=max(lst)
minl=min(lst)
for i in lst:
    if i==maxl or i==minl:
        lst.remove(i)
print(lst)
