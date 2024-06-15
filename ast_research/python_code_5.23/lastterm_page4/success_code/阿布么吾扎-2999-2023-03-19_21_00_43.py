ls=input().split(' ')
n,m=input().split(' ')
lst=list(ls)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
