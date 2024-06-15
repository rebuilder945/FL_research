A=input().split(' ')
n,m=input().split(' ')
n=int(n)
m=int(m)
lst=list(A)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
