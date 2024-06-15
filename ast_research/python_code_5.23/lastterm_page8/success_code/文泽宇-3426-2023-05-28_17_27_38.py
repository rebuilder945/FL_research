x = eval(input())
if x <20:
    n=6*(x**2)+1
    print('{:.2f}'.format(n))
elif x<40:
    n=((3*x)-60)**0.5
    print('{:.2f}'.format(n))
else:
    n=100/(x+1)
    print('{:.2f}'.format(n))
