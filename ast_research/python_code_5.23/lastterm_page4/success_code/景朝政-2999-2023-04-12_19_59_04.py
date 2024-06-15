A=input().split('')
n,m=inputO().split('')
lst=list(A)
n=int(n)
m=int(m)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
