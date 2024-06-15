lst=eval(input())
maxi=max(lst)
mini=min(lst)
a=lst.copy()
for i in lst:
    if i==maxi or i == mini:
        a.remove(i)
print(a)
