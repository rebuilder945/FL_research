lst=eval(input())
a=min(lst)
b=max(lst)
while a in lst:
    lst.remove(a)
while b in lst:
    lst.remove(b)
print(lst)
