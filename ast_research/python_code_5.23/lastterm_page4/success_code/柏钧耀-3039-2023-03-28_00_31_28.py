lst=eval(input())
a=lst.count(min(lst))
b=lst.count(max(lst))
for i in range(a):
    c=lst.index(min(lst))
    del lst[c]
for i in range(b):
    d=lst.index(max(lst))
    del lst[d]

print(lst)
































