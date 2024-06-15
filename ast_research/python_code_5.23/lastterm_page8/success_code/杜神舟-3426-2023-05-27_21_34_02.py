def f(n):
    if n<20:
        n=6*n**n+1
    elif 20<=n<40:
        (3*n-60)**(1/2)
    else:
        n=100/(n+1)
    print('%.2f'%n)

n=eval(input())
f(n)
