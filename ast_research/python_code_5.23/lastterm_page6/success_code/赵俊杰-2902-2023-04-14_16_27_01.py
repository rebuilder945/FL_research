n=eval(input())
a=2
b=1
s=0
while n>0:
    s=s+a/b
    a=a+b
    b=a-b
    n=n-1
print("%.4f"%(s))
