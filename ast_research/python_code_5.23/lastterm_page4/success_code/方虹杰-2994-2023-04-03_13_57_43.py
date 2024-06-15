a=input().split(",")
a=[int(a[i]) for i in range (len(a))]
n,m=eval(input())
if n+1>len(a) or (-n)>len(n):
    print("error")
else:
    b=[a[n]*m]
    print(a+b)
