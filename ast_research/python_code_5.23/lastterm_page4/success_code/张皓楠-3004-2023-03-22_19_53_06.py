a = eval(input())
for c in a:
    if c > 2:
        for i in range(2,c):
            if c%i==0:
                a.remove(c)
print(a)
