lst=list(input().split(" "))
n,m=map(int,input().split())
num1=lst[n]
num2=lst[m]
t=num1
lst[n]=num2
lst[m]=t
print(lst)
