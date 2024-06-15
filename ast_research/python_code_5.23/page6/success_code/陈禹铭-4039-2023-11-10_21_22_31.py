x=float(input())
if x<20:
    y=6*x**2+1
    print('%.2f'%y)
elif 20<x<40 or x==20:
    y=(3*x-60)**0.5
    print('%.2f'%y)
elif x>=40:
    y=100/(x+1)
    print('%.2f'%y)
