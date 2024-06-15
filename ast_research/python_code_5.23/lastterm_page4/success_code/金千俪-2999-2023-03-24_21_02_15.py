lst=input().split()
n,m=map(int,input().split())
n<=len(lst) and m<=len(lst)
t = lst[m]
lst[m]=lst[n]
lst[n]=t
print(lst)

