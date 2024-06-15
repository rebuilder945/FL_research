lst=eval(input())
a=max(lst)
b=min(lst)
if a in lst :
    lst.remove(a)
if b in lst :
    lst.remove(b)
print(lst)
