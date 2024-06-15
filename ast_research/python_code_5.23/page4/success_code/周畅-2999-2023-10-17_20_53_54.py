lst=input()
n,m=input().split()
n=int(n)
m=int(m)
lst[n],lst[m]=lst[m],lst[n]
lst=list(lst)
print(lst)
