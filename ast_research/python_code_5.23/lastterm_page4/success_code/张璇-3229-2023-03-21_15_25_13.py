a=eval(input())
for x in a:
    b=a.count(x)
    while b>1:
        a.remove(x)
        b=a.count(x)
        if b==1:
            a.remove(x)
    b=a.count(x)
if b==0:
    c=a.sort()
    print(a)
