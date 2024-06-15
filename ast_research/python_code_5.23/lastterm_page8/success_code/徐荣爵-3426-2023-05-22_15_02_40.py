x = eval(input())
if x < 20:
    t = 6*x**2 + 1
elif x < 40:
    t = (3 * x - 60) ** 0.5
else:
    t = 100/(x+1)
print('%.2f'%t)
