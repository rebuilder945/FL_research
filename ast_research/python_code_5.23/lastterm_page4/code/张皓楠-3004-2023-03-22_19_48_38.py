a = eval(input())
for c in a:
    if c >2:
        for i in range(2,c):
            while c%i==0:
                del a(a.index(c))
print(a)
