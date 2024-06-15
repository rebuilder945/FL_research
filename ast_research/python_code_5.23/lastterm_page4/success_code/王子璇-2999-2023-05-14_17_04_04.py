lst=input().split()
n,m=input().split()
n=int(n)
m=int(m)
lst[m],lst[n]=lst[n],lst[m]
print(lst)
