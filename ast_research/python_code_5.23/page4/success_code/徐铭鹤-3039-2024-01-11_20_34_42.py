a=eval(input())
b=a.count(max(a))
c=a.count(min(a))
for i in range(b):
    del a[a.index(max(a))]
for i in range(c):
    del a[a.index(min(a))]
print(a)

    


