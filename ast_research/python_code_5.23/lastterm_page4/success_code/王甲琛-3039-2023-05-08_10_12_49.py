lst=eval(input())
a=max(lst)
b=min(lst)
while max(lst)==a:
    lst.remove(a)
while min(lst)==b:
    lst.remove(b)
print(lst)
    
