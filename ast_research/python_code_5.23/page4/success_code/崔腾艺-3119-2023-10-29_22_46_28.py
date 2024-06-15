a=eval(input())
for x in a:
    b=a.count(x)
    while b>=2:
        b-=1
        a.remove(x)
print(a)
