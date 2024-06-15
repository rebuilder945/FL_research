def hanshu(x):
    a=0
    if x <20:
        a=6*x**2+1
    elif x<40:
        a=(3*x-60)**(1/2)
    else:
        100/(x+1)
    return a
x=eval(input())
print('%.2f'%(hanshu(x)))
