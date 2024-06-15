lst=list(input())
n,m=eval(input())
a=lst[n]
b=lst[m]
lst[n]=b
lst[m]=a
print(lst)
