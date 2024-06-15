a = eval(input())
for i in a:
    if a.count(a)>1:
        b = a.count(i-1)
        for x in range(b):
            del a[a.index(i)]
print(a)

