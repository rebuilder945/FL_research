n = eval(input())
if n < 20:
    a = 6*n**2 + 1
elif 20<=n<40:
    a = (3*n - 60)**0.5
else:
    a = 100/(n+1)
print('%.2f'%a)
