lst=eval(input())
a=lst.count(max(lst))
b=lst.count(min(lst))
if a>0:
    for i in range(a):
    lst.remove(max(lst))
if b>0:
    for i in range(b):
    lst.remove(min(lst))
print(lst)
