n=eval(input())
if n<20:
    y=6*n**2+1
    print('%.2f'%(y))
elif n<40:
    y=(3*n-60)**(1/2)
    print('%.2f'%(y))
else:
    y=100/(n+1)
    print('%.2f'%(y))

