def f(t):
    if t<20:
        r=6*t**2+1
    elif 20<=t<40:
        r=(3*t-60)**0.5 
    elif 40<=x:
        r=100/(t+1)
    return r
x=eval(input())
y=f(x)
print('%.2f'%y)
