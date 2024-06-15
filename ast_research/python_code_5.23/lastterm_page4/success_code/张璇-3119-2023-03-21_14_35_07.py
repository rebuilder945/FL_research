a=eval(input())
for x in a:
    b=a.count(x)
    while b>=2:
        b=a.count(x)
        a.remove(x)
        if b==2:
            break
print(a)
