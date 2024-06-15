x=int(input())
if x<20:
    a=6*x**2+1
    print('%.2f'%(a))
elif 20<=x and x<40:
    a=(3*x-60)**0.5
    print('%.2f'%(a))
elif x>=40:
    a=100/(x+1)
    print('%.2f'%(a))

