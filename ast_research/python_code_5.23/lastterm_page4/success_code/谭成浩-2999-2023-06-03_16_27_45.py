date=input().split(" ")
n1,n2=input().split(" ")
lst=list(date)
m1=lst[n1]
m2=lst[n2]
lst[n1]=m2
lst[n2]=m1
print(lst)

