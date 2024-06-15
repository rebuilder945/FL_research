lis=eval(input())
a,b=eval(input())
l=[]
c=len(lis)
if a>=c or b>=c:
    print("error")
else:
    d=lis[a:b]
    for x in lis:
        if x in d:
            pass
        else:
            l.append(x)
    print(l)
