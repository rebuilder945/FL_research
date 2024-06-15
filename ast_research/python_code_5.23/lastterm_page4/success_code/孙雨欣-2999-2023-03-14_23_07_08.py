ls1=input().split(" ")
m,n=input().split(" ")
m=int(n)
n=int(n)
ls3=[]
ls3=ls1[m]
ls1[m]=ls1[n]
ls1[n]=ls3
print(ls1)
