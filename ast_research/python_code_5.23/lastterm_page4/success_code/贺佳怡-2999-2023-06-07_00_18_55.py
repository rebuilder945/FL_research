a=list(input().split())
n,m=eval(input().split())
if n>len(a) or m>len(a):
    print("error")
elif len(a)>n and len(a)>m:
    c=a[n]
    a[n]=a[m]
    a[m]=c
    print(a)
else:
    print("error")

