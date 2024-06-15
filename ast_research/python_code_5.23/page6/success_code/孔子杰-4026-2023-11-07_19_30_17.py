n=eval(input())
a,b=2,1
sum=0
for i in range(1,n+1):
    sum=sum+a/b
    a,b=a+b,a
print("%.4f"%(sum))

