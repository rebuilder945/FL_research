a=eval(input())
a1=a.copy()
for x in a:
    b=a.count(x)
    if b>1:
        a1.remove(x)
if len(a1)>=1:
    a1.sort()
    a1=[str(x) for x in a1]
    ",".join(a1)
    print(a1)
elif len(a1)==0:
    print(False)
