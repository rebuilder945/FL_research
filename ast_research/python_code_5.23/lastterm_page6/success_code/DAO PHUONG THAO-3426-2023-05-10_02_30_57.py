import math
x=eval(input())
if x<20:
   res=6*(x**2)+1
elif x>=20 and x<40:
   res = math.sqrt(3*x-60)
else:
   res=100/(x+1)
print("%.2f"%res)

