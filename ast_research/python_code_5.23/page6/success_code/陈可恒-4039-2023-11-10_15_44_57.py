x = eval(input())
if x < 20:
    print('%.2f'%(1+6*x*x))
elif 20<= x <40:
    print('%.2f'%((3*x-60)**(1/2)))
else :
    print('%.2f'%(100/(x + 1)))
