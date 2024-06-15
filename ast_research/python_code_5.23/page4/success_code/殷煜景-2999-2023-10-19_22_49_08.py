a=list(input().split(" "))
n,m=input().split(" ")
n=int(n)
m=int(m)
a[m],a[n]=a[n],a[m]
print(a)
