lst = eval(input())
a = max(lst)
b = min(lst)
lst1=lst.copy()
for x in lst1:
    if x==a or x==b:
        lst.remove(x)
print(lst)
