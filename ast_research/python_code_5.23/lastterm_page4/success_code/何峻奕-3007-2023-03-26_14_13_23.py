a=eval(input())
n,m=eval(input())
if n<m:
    del a[n,m]
    print(a)
if n>m:
    print("error")
elif n or m > len(a):
    print("error")

