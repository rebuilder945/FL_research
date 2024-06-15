lst=input().split()
n,m=map(int,input().split())
lst1=lst.copy
lst1[n],lst1[m]=lst[m],lst[n]
print(lst1)
