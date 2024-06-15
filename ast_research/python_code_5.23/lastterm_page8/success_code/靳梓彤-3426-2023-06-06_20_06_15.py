x=eval(input())
if x<20:
    y=6*(x**2)+1
elif x<40 and x>=20:
    y=(x*3-60)**0.5
else:
    y=100/(x+1)
print("%.2f"%y)
