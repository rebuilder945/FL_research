lst=input().split()
n,m=map(int,input().split())
temp=lst[n]
lst[n]=lst[m]
lst[m]=temp
print(lst)
