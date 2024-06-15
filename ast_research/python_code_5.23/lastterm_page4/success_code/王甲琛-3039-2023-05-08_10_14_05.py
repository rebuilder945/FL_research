lst=eval(input())
a=max(lst)
b=min(lst)
if len(lst)>=2:
    while max(lst)==a:
        lst.remove(a)
    while min(lst)==b:
        lst.remove(b)
else:
    lst.clear()
print(lst)
    
