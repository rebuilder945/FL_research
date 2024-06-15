a=eval(input())
n,m=eval(input())
c=int(m)
b=int(n)
q=a[c]
a[c]=a[b]
a[b]=q
print(a)
