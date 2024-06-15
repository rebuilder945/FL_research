a=input().split(" ")
f=eval(input()).split(" ")
for n,m in f:
    b=a.insert(n,a[m])
    c=b.remove(m+1)
    d=c.insert(m,a[n+1])
    e=d.remove(n+1)
print(e)
