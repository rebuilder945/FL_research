
lst=input().split()
n,m=map(int,input().split())
a=lst[n]
b=lst[m]
lst[n],lst[m]=b,a
print(lst)
