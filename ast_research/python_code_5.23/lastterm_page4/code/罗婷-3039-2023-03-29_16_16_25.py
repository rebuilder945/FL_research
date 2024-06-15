lst=eval(input())
smax=max(lst)
smin=min(lst)
lst1=lst.copy()
for i in lst:
    if i==smas or i=smin:
        lst1.remove(i)
print(lst1)
