def f(x):
    if x<20:
        print('%.2f'%(6*x*x+1))
    elif 20<=x<40:
        print('%.2f'%((3*x-60)**0.5))
    else:
        print(100/(x+1))
x=eval(input())
f(x)
