x = eval(input())
if x < 20:
    fx = 6*x*x+1
elif x >= 40:
    fx = 100/(x+1)
else:
    fx = (3*x-60)**0.5
print('%.2f'%fx)
