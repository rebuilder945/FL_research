a=eval(input())
a1=a.copy()
for x in a:
    b=a.count(x)
    if b>1:
        a1.remove(x)
if len(a1)>=1:
    a1.sort()
    print(a1)
elif len(a1)==0:
    print(False)
