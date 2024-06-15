x=eval(input())
if x<20:
    n=6*x**2+1
elif 20<=x<=40:
    n=(3*x-60)**0.5
elif x>=40:
    n=100/(x+1)
else:
    n=0
print("%.2f"%(n))
