import math
x=eval(input())
if x<20:
    f=6*pow(x,2)+1
elif 20<=x<40:
    f=math.sqrt(3*x-60)
elif x>=40:
    f=100/(x+1)
print("%.2f"%f)
