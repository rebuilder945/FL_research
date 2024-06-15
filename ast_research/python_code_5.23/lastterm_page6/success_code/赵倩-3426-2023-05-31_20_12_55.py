a=eval(input())
if a<20:
    f=6*(a**2)+1
elif 20<=a<40:
    f=(3*a-60)**(1/2)
else:
    f=100/(a+1)
print("%2.f"%f)
