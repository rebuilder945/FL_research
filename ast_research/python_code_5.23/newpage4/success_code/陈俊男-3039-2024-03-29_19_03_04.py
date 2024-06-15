lst=eval(input())
lst1=lst.copy()
a=max(lst)
b=min(lst)
for n in lst:
    if n==a or n==b:
        lst1.remove(n)
print(lst1)
