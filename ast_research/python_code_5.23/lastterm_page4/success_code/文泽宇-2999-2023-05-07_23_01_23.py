a=input().split(' ')
n,m=eval(input())
c=a[int(n)]
a[int(n)]=a[int(m)]
a[int(m)]=c
print(a)
