a=list(input().split(","))
n,m=eval(input())
for x in a:
    x=int(x)
if n>=0:
    if n<len(a):
        for i in range(m):
            a.append(a[n])
        print(a)
    else:
        print("error")
else:
    if (-n)<=len(a):
        for i in range(m):
            a.append(a[n])
        print(a)
    else:
        print("error")
