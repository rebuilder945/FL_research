list=input().split(" ")
n,m=input().split(" ")

exchange1=list[m]
exchange2=list[n]

list[n]=exchange1
list[m]=exchange2
print(list)
