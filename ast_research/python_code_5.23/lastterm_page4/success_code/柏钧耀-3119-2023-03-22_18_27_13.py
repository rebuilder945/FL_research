a=eval(input())
b=a[::]
for x in range(len(a)):
    c=a.count(a[x])
    if c>1:
        for i in range(c-1):
            b.remove(a[x])

print(b)


