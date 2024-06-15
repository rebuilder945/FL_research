x=float(input())
if x<20:
    a=6*x*x+1
elif 20<=x<40:
    a=(3*x-60)**(1/2)
elif x>=40:
    a=100/(x+1)
print('%.2f'%a)
