lst=eval(input())
a=max(lst)
b=min(lst)
for x in lst:
    while a in lst:
        lst.remove(a)
    while b in lst:
        lst.remove(b)
    print(lst)
