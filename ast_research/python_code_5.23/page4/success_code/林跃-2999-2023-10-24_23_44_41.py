lst=list(input().split())
n,m=input().split()
n=int(n)
m=int(m)
lst1=lst.copy()
lst1[m]=lst[n]
lst1[n]=lst[m]
print(lst1)
