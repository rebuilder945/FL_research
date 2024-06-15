x=eval(input())
if x<20:
    y=6*(x^2)+1
elif x>=20 and x<40:
    y=(3*x-60)^(1/2)
elif x>=40:
    y=100/(x+1)
print("%.2f"%(y))
