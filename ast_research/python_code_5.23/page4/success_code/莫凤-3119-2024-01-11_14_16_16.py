a=eval(input())
for x in reversed(a):
    n=a.count(x)
    if n>1:
        del a[a.index(x)]
print(a)
