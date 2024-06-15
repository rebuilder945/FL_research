a=eval(input())
if a<20:
    print("%.2f"%(6*a**2+1))
elif 20<=a<40:
    print("%.2f"%(pow(3*a-60,0.5)))
else:
    print("%.2f"%(100/(a+1)))
