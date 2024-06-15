lst1=input().split()
lst=list(lst1)
n,m=input().split()
n=int(n)
m=int(m)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
