list=input().split(',')
n,m=eval(input())
x=list[n]
y=list[m]
list[n]=y
list[m]=x
print(list)
