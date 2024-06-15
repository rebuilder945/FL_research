a=eval(input())
for x in a:
    if a.count(x)!=1:
        while x in a:
            a.remove(x)
        a.sort()
for x in a:
    if a.count(x)!=1:
        while x in a:
            a.remove(x)
        a.sort()
    b=a
if not b:
    print(False)
else:
    c=','.join(str(x)for x in b)
    print(c)
