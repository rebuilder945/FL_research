lst=input().split(",")
n,m=eval(input())
lst=list(lst)
n,m=int(n,m)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
