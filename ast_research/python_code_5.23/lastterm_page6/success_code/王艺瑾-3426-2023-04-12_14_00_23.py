x=eval(input())
if x<20:
    y=6*(x**2)+1
elif x in range(20,40):
    y=(3*x-60)**0.5
else:
    y=100/(x+1)
print("%.2f"%(y))


