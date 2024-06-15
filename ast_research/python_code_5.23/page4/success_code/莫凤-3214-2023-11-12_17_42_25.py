a=eval(input())
b=a.count(0)
if b>1:
    for x in range(1,b+1):
        del a[a.index(0)]
        a.append(0)
print(a)
