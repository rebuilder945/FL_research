list=input().split(' ')
n,m=input().split(' ')
n=int(n)
m=int(m)
x=list[n]
y=list[m]
list[n]=y
list[m]=x
print(list)
