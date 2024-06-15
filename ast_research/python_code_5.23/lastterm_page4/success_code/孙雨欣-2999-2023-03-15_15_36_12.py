ls1=input().split(" ")
m,n=input().split(" ")
m=int(m)
n=int(n)
a=" "
a=ls1[m]
ls1[m]=ls1[n]
ls1[n]=a
print(ls1)
