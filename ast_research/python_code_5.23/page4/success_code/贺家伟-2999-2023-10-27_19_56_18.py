l=input().split(" ")
m,n=input().split(" ")
m=eval(m)
n=eval(n)
t=l[m]
l[m]=l[n]
l[n]=t
print(l)
