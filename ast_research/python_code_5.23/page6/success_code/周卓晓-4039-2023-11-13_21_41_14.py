x=eval(input())
if x<20:
    y=6*x*x+1
elif 20<=x<40:
    y=(3*x-60)**0.5
else:
    y=100/(x+1)
print("%.2f"%(y))


