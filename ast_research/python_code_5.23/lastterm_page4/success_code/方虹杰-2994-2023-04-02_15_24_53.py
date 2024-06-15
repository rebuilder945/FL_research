a=input().split(",")
n,m=eval(input())
if n+1>len(a) or (-n)>len(a):
    print("error")
else:
    b=[a[n]*m]
    print(a+b)
