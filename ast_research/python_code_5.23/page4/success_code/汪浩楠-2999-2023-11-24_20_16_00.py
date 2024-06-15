a=input().split()
n,m=eval(input())
lst1=list(a)
b=lst1[n]
lst1[n]=lst1[m]
lst1[m]=b
print(lst1)

