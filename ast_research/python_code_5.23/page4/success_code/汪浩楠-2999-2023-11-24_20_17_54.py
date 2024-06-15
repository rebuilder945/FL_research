a=input().split()
n,m=input().split()
lst1=list(a)
b=lst1[n]
lst1[n]=lst1[m]
lst1[m]=b
print(lst1)

