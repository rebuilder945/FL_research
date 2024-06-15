a=eval(input())

for x in a:
    b=a.count(x)
    if b!=1:
        for y in range(b-1):
            a.remove(x)
    else:
        continue
print(a)


