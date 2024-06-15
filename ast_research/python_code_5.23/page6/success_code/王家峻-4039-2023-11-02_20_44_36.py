x=eval(input())
if x<=19:
    c=6*x**2+1
    print('%.2f'%(c))
elif x>=20 and x<=40:
    b=(3*x-60)**0.5
    print('%.2f'%(b))
elif x>=41:
    y=100/(x+1)
    print('%.2f'%(y))
