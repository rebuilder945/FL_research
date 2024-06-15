a=eval(input())
for x in reversed(a):
    if a.count(x)>1:
        for y in range(1,a.count(x)):
            del a[a.index(x)]
print(a)
