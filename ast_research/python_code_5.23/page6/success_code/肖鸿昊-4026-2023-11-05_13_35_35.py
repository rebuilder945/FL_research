n=eval(input())
a=1
b=2
d=2
e=3
p=[]
q=[]
r=[]
if n==1:
    n=2.0000
    print(".4f"%(n))
else:
    for i in range(n-1):
        s=b
        b=a+b
        a=s
        p.append(a)
        f=e
        e=d+e
        d=f
        q.append(e)
        p.insert(0,1)
        q.insert(0,2)
        q.insert(1,3)
    for x in range(n):
        t=q[-x-2]/p[-x-1]
        r.append(t)
    y=sum(r)
    print("%.4f"%(y))
