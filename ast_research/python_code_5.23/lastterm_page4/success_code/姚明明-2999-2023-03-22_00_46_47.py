list=input().split(",")
n,m=map(int,input().split())
x=list[n]
list[n]=list[m]
list[m]=x
print(list)
