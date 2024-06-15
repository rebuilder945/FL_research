a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
        b.sort()
        if not b:
            print(False)
        else:
            c=','.join(str(x)for x in b)
            print(c)
