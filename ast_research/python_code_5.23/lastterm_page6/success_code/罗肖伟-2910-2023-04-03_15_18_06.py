x=eval(input())
y=eval(input())
if y==1:
   s=x
else:
 s=x
 for i in range(y-1):
    x*=0.5
    s+=2*x
print("%.2f"%(s))

