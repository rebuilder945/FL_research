a=input().split(sep=" ")
sz=input().split(sep=" ")
n=eval(sz[0])
m=eval(sz[-1])
q=a[n]
p=a[m]
a[n]=p
a[m]=q
print(a)
