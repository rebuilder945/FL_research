lst=str(input().split())
n,m=eval(input().split())
lst1=lst.copy()
lst1[m]=lst[n]
lst1[n]=lst[m]
print(lst1)
