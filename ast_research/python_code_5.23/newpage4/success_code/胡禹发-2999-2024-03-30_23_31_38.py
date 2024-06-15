a=list(input().split(" "))
b=list(input().split(" "))
n,m=eval(b[0]),eval(b[1])
c=a[n]
d=a[m]
if n<m:
    a.remove(c)
    a.remove(d)
    a.insert(n,d)
    a.insert(m,c)
else:
    a.remove(c)
    a.remove(d)
    a.insert(m,c)
    a.insert(n,d)
print(a)
