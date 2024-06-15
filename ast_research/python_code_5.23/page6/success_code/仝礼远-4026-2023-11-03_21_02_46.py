m=1
n=2
s=0
N=eval(input())
for i in range(N):
    a=n/m
    b=m
    m=n
    n=n+b
    s=s+a
print("%.4f"%(s))
    
