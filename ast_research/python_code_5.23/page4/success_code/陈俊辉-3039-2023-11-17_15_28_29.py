a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
if len(a)>0:
    for x in ranage(b):
     del a[a.index(max(a))]
    for x in range(c):
     del a[a.index(min(a))]
print(a)


