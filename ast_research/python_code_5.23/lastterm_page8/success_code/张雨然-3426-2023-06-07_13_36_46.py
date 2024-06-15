def f(x):
    if x<20:
        result=6*x**2+1
    elif 20<=x<=40:
        result=(3*x-60)**1/2
    else:
        result=100/(x+1)
    return result

i=float(input())
print('%.2f'%f(i))
