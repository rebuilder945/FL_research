a=input().split()
n,m=input().split()
n=int(n)
m=int(m)
lst1=list(a)
b=lst1[n]
lst1[n]=lst1[m]
lst1[m]=b
print(lst1)

