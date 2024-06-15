lst=input().split(",")
n,m=eval(input())
lst=list(lst)
lst[n],lst[m]=lst[m],lst[n]
print(lst)
