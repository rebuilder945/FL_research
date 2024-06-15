a=eval(input())
for x in a:
    if a.count(x)!=1:
        while x in a:
            a.remove(x)
        a.sort()
    n=a
for x in n:
    if n.count(x)!=1:
        while x in n:
            n.remove(x)
        n.sort()
    b=n
if not b:
    print(False)
else:
    c=','.join(str(x)for x in b)
    print(c)
