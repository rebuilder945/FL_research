a=input()
n,m=map(int,input().split())
list=a.split()
b=list[n]
list[n]=list[m]
list[m]=b
print(list)
