a=list(input())
b=list(input().split(" "))
n,m=eval(b[0]),eval(b[1])
c=a[n]
d=a[m]
a.remove(c)
a.insert(n,d)
a.remove(d)
a.insert(m,c)
