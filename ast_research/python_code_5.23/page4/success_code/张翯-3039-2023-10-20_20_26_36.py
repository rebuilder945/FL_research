lst=eval(input())
a=max(lst)
while a in lst:
    lst.remove(a)
b=min(lst)
while b in lst:
    lst.remove(b)
print(lst)
