list=input().split()
m,n=input().split()
x=int(m)
y=int(n)
a=list[x]
list[x]=list[y]
list[y]=a
print(list)
