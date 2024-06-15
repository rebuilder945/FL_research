x=eval(input())
if x<20:
    res=6*(x**2)+1
elif 20<=x<40:
    res=(3*x-60)**0.5
else:
    res=100/(x+1)
print("%.2f"%res)
    
