def f(t):
    if t<20:
        m=6*(t**2)+1
    elif t<40:
        m=(3*t-60)**0.5
    else:
        m=100/(t+1)
    return m
y=f(eval(input()))
print('%.2f'%y)
