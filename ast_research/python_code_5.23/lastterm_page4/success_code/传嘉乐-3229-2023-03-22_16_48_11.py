a=eval(input())
for x in a:
    if a.count(x)!=1:
        while x in a:
            a.remove(x)
        a.sort()
        if not a:
            print(False)
        else:
            c=','.join(str(x)for x in a)
            print(c)



