a=list(input().split())
n,m=input( ).split(' ')
a[eval(n)],a[eval(m)]=a[eval(m)],a[eval(n)]
print(a)
