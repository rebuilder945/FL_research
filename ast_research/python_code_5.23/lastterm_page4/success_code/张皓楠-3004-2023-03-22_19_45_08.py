a = eval(input())
b = a[1:]
for c in b:
    if c >2:
        for i in range(2,c):
            while c%i==0:
                b.remove(c)
print(b)
