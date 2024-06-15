a=list(input().split(" "))
b=list(input().split(" "))
n,m=eval(b[0]),eval(b[1])
a[n],a[m]=a[m],a[n]
print(a)
