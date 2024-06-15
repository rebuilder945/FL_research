a=int(input())
b=int(input())
c=int(input())
sum,pinjun=a+b+c,(a+b+c)/3
pinjun="%.2f"%(pinjun)
A=sum,pinjun
print(A.split(","))
