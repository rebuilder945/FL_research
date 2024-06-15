ls=input().split()
m,n=map(int,input().spilt())
ls1=ls[:]
ls[m]=ls1[n]
ls[n]=ls1[m]
print(ls)
