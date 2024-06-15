a=input().split()
n,m=map(int,input().split())
lst=list(a)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
