a=[]
a.extend(input().split())
n,m=eval(input())
N=a[n]
M=a[m]
a[n]=M
a[m]=N
print(a)
