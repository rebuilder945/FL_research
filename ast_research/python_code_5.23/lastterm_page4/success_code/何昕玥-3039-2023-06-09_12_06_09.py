lst=eval(input())
sMax=max(lst)
sMin=min(lst)
lst1=lst.copy()
for i in lst:
    if i==sMax or i==sMin:
        lst1.remove(i)
print(lst1)


