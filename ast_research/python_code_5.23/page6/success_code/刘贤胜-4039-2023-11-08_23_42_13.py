import math
n1=eval(input())
if n1<20:
    n1=6*n1**2+1
elif 20<=n1<40:
    n1= math.sqrt(3*n1-60)
elif n1>=40:
    n1=100/(n1+1)
print("%.2f"%(n1))
