lst=eval(input())
a=max(lst)
b=min(lst)
lst1=lst.copy()

for i in lst1:
    if i==a or i==b:
        lst.remove(i)
print(lst)

