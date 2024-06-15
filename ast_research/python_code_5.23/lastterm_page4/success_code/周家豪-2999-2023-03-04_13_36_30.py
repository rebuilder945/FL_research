lst=input().split(" ")
nm=input().split(" ")
nm=list(map(int,nm))
m=nm[0]
n=nm[1]

exchange1=lst[m]
exchange2=lst[n]

lst[n]=exchange1
lst[m]=exchange2
print(lst)
