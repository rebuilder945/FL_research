lst=eval(input())
a=max(lst)
b=min(lst)
if a!=b :
    while max(lst)==a:
        lst.remove(a)
    while len(lst)>=1 and min(lst)==b:
        lst.remove(b)
else:
    lst.clear()
print(lst)
    
