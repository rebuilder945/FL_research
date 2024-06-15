lst=eval(input())
a=max(lst)
b=min(lst)
c=lst.count(a)
d=lst.count(b)
for i in range(0,c):
    lst.remove(a)
for i in range(0,d):
    lst.remove(b)
print(lst)
