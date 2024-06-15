l=input().split(" ")
m,n=input().split(" ")
m=int(m)
n=int(n)
t=str(l[n])
l[n]=m
l[m]=t
print(l)
