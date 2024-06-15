a=list(input().split(","))
n,m=eval(input())
b=[]
c=a.copy()
if n>=0:
    if n<len(c):
        for i in range(m):
            a.append(c[n])
        for x in a:
            x=int(x)
            b.append(x)
        print(b)

    else:
        print("error")
else:
    if (-n)<=len(c):
        for i in range(m):
            a.append(c[n])
        for x in a:
            x=int(x)
            b.append(x)
        print(b)
    else:
        print("error")
