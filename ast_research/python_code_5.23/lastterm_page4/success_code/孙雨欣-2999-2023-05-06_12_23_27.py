ls1=input().split()
m,n=map(int,input().split())
ls1[m]=ls1[n]
ls1[n]=ls1[m]
print(ls1)
