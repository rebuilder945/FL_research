ls=input().split(" ")
m,n=map(int,input().split(" "))
ls1=ls.copy()
ls1[m]=ls[n]
ls1[n]=ls[m]
print(ls1)
