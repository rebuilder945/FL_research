n=list(map(int,input().split(",")))
a,b=input().split(",")
a=int(a)
b=int(b)
e=len(n)-1
f=len(n)*(-1)
if a>e or a<f:
    print("error")
else:
    c=n.count(n[a])
    d=n[a]
    for i in range(b):
        n.append(d)
    print(n)


