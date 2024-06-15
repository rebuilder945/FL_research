lst=input().split() 
n,m=map(int,input().split())
lst[n],lst[m]=lst[m],lst[n]
print(lst)
