a=eval(input())
a.sort(reverse=True)
n=len(a)-1
d=[]
if 0 not in a:
    for i in range(n):
        s=a[i]*10**(n-i)
        d.append(s)
    m=sum(d)+1
    print(m)
else:
    for i in range(n):
        s=a[i]*10**(n-i)
        d.append(s)
    m=sum(d)
    print(m)
