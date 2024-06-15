lst=eval(input())
a=max(lst)
b=min(lst)
if a!=b:
    while max(lst)==a:
        lst.remove(a)
    while min(lst)==b:
        lst.remove(b)
else:
    lst.clear()
print(lst)
    
