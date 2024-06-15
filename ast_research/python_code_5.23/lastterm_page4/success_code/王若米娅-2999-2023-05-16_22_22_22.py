str=input()
c=str.split()
lst=list(c)
n,m=map(int,input().split())
a=lst[n]
b=lst[m]
lst[n]=b
lst[m]=a
print(lst)

