x = eval(input())
if x<20:
    result=6*x**2+1
elif x<40 and x>=20:
    result=(3*x-60)**0.5
elif x>=40:
    result=100/(x+1)
print("%.2f"%result)

