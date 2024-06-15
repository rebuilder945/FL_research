lst=eval(input())
a=max(lst)
b=min(lst)
while a in lst:
    lst.remove(a)
    lst.remove(b)
print(lst)
