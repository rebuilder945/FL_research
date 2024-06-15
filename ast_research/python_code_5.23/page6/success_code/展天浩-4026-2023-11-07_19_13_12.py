n=eval(input())
a=2
b=1
sum=0
while n>0:
    sum+=a/b
    a,b=a+b,a
    n-=1
print("%5.4f"%(sum))
