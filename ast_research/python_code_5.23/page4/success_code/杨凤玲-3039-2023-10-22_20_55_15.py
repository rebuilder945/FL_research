lst=eval(input())
lst.sort()
maxl=max(lst)
minl=min(lst)
for i in lst:
    if i==maxl or i==minl:
        lst.remove(i)
print(lst)
