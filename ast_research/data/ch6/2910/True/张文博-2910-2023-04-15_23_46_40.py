m=eval(input())
n=eval(input())
x=m
if n==1:
    print("%.2f"%x)
else:
    for i in range(n-1):
        x=x+2*m*0.5**(i+1)
        
    print("%.2f"%x)
