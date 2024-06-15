x=eval(input())
if x<20:
    t=6*x*x+1
elif x>=40:
    t=100/(x+1)
else:
    t=(3*x-60)**(0.5)
print("{:.2f}".format(t))
