a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
        b.sort()
        c=''.join(map(str,b))
        print(c)
        break
    else:
        print("False")
