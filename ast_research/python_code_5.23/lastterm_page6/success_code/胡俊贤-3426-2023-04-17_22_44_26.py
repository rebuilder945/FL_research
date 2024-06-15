x=eval(input())
def f(x):
    if x<20:
        return 6*x*x+1
    elif x>=20 and x<40:
        return (3*x-60)**(1/2)
    else:
        return 100/(x+1)
print('%.2f'%f(x))

