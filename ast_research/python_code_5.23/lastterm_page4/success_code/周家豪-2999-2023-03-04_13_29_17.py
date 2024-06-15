list=input().split(" ")
n,m=eval(input())

exchange1=list[m]
exchange2=list[n]

list[n]=exchange1
list[m]=exchange2
print(list)
