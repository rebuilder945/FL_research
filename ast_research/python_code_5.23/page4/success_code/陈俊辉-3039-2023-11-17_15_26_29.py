a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
if len(a)>0:
    del a[a.index(max(a))]
    del a[a.index(min(a))]
print(a)


