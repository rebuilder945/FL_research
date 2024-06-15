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
    for x in c:
        x=str(x)
    a=",".join(c)
    print(a)
