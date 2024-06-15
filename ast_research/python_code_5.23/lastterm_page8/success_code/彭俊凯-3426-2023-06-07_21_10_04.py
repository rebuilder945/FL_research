n=eval(input())
if n<20:
    print('%.2f'%(6*n**2+1))
elif 20<=n<40:
    print('%.2f'%((3*n-60)**0.5))
else:
    print('%.2f'%(100/(n+1)))
