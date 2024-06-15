a=list(input().split(" "))
b=list(input().split(" "))
n,m=eval(b[0]),eval(b[1])
c=a[n]
d=a[m]
a.remove(c)
a.insert(n+1,d)
a.remove(d)
a.insert(m+1,c)
print(a)
