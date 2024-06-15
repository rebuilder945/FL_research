a=list(input())
n,m=eval(input())
b=months[n]
c=months[m]
del a[n]
del a[m]
a.insert(n,c)
a.insert(m,b)
print(a)
