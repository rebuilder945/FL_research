h=eval(input())
n=eval(input())
if n==1:
    print("%.2f"%(h))
else:
    a=1
    for i in range(n-1):
        a=a+(0.5)**i
    print("%.2f"%(a*h))
