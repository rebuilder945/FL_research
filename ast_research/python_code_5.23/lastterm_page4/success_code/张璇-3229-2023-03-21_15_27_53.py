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
    a.sort()
    for x in a:
        x=str(x)
    a=",".join(a)
    print(a)
