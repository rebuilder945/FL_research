names=list(input().split(" "))
n,m=input().split(" ")
n=eval(n)
m=eval(m)
tmp=names[n]
names[n]=names[m]
names[m]=tmp
print(names)
