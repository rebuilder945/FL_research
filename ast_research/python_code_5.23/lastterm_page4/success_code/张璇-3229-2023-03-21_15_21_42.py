a=eval(input())
for x in a:
    b=a.count(x)
    while b>1:
        a.remove(x)
        b=a.count(x)
        if b==1:
            a.remove(x)
    b=a.count(x)
if b==1:
    c=",".join(a.sort())
    print(a)
elif b==0:
    print("False")
