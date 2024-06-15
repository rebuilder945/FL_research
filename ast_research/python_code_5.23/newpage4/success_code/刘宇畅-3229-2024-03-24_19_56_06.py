a=eval(input())
b=a[0:-1]
if b.count(a)==1:
    d=list(c)
    d.sort()
    print(d)
elif b.count(a)>1:
    print("False")

