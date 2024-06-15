ls1=input().split(" ")
m,n=input().split(" ")
ls1=list(ls1)
m=int(n)
n=int(n)
ls1[n],ls1[m]=ls1[m],ls1[n]
print(ls1)
