def result(x):
    if x<20:
        k=6*x**2+1
    elif  x>=20 and x<40:
        k=(3*x-60)**0.5
    else:
        k=100/(x+1)
    return k
m=eval(input())
print('%.2f'%(result(m)))
