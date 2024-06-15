a=list(input().split(","))
n,m=eval(input())
b=[]
if n>=0:
    if n<len(a):
        for i in range(m):
            a.append(a[n])
        for x in a:
            x=int(x)
            b.append(x)
        print(b)

    else:
        print("error")
else:
    if (-n)<=len(a):
        for i in range(m):
            a.append(a[n])
        for x in a:
            x=int(x)
            b.append(x)
        print(b)
    else:
        print("error")
