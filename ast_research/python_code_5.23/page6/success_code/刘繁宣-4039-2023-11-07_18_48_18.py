n=eval(input())
if n<20:
    n=6*n**2+1
elif 20<=n<40:
    n=(3*n-60)**0.5
else:
    n=100/(n+1)
print('%.2f'%n)
