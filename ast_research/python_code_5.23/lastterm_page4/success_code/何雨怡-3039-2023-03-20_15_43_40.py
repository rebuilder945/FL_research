lst=eval(input())
lst2=lst.copy()
a=max(lst)
b=min(lst)
for i in lst2:
    if i==a or i==b:
        lst.remove(i)
    else:
        pass
print(lst)
