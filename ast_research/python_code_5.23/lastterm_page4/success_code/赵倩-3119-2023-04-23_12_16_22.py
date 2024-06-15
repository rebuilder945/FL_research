a = eval(input())
d = a.copy()
for x in a:
    b = d.count(x)
    if b>=2:
        while b>=2:
            d.remove(x)
            b-=1
print(d)
