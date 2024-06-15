a=eval(input())
for x in a:
    b=a.count(x)
    while b>1:
        a.remove(x)
    c=a.count(x)
if c==1:
    a.sort()
    print(a)
elif c==0:
    print("False")
