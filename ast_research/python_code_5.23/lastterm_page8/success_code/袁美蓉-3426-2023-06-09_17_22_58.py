def f(a):
    if a<20:
        y = 6*a**2+1
    elif a>=20 and a<40:
        y = (3*a-60)**0.5
    elif a>40:
        y = 100/(a+1)
    return y
x = eval(input())
print('%.2f'%f(x))


