lst=eval(input())
a=max(lst)
b=min(lst)
for i in lst[0:]:
    if i==a:
        lst.remove(a)
    if i==b:
        lst.remove(b)
print(lst)
