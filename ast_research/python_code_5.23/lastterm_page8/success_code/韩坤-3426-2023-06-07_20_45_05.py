import math
x=eval(input())
s=0
if x<20:
    s=s+(6*x**2+1)
elif x>=40:
    s=s+100/(x+1)
else:
    s=s+math.sqrt(3*x-60)
print("{:.2f}".format(s))

