a=eval(input())
for x in a:
    b=a.count(x)
    while b>=2:
        a.remove(x)
        b=a.count(x)
        if b==2:
            break
print(a)
