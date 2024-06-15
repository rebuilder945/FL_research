a=eval(input())
c=[]
n,m=eval(input())
if n<=len(a):
    for x in a:
        c.append(x)
    b=a[n]
    for i in range(m):
        c.append(b)
    print(c)
else:
    print("error")
