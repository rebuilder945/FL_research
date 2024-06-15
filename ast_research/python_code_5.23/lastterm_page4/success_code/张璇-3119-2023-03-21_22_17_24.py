a=eval(input())
a1=a.copy()
for x in a:
    b=a.count(x)
    while b>1:
        a1.remove(x)
        b=a1.count(x)
        if b==1:
            break
if b==0:
    a1.sort()
    print(a1)
