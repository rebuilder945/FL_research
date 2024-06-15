x=eval(input())
if x<20:
    A=pow(x,2)
    y=6*A+1
if 20<=x<40:
    y=pow(3*x-60,1/2)
if x>=40:
    y=100/(x+1)
print("%.2f"%y)




