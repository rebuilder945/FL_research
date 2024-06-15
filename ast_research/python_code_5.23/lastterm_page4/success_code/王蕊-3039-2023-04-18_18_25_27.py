lst=eval(input())
a=max(lst)
b=min(lst)
ls2=lst.copy()
for x in ls2:
    if x==a or x==b:
        lst.remove(x)
print(lst)

