a=eval(input())
for x in a:
    if a.count(x)!=1:
        while x in a:
            a.remove(x)
        b=a.sort()
        if not b:
            print(False)
        else:
            c=','.join(str(x)for x in b)
            print(c)



