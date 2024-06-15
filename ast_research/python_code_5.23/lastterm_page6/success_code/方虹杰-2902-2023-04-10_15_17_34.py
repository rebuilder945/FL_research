n=int(input())
a,b,sum=2,1,0
for i in range(n):
    sum=sum+a/b
    a,b=a+b,a
print("%.4f"%(sum))

