x=eval(input())
if x<20:
    a=6*(x**2)+1
    print('{:.2f}'.format(a))
elif 20<=x<40:
    b=(3*x-60)**0.5
    print('{:.2f}'.format(b))
elif x>=40:
    c=100/(x+1)
    print('{:.2f}'.format(c))
