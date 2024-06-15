lst=input().split("")
n,m=eval(input()).split("")
lst=list(lst)
n,m=int(n,m)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
