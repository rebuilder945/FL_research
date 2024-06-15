a=input().split("")
n,m=input().split("")
lst1=list(a)
n=int(n)
m=int(m)
lst1[n],lst1[m]=lst1[m],lst1[n]
print(lst1)
