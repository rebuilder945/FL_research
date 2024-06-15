def hanshu(x):
    if x<20:
        aim = 6*x**2+1
        return aim
    elif 20<=x<40:
        aim = (3*x-60)**0.5
        return aim
    elif x>=40:
        aim = 100/(x+1)
        return aim


x = eval(input())
print('%.2f'%hanshu(x))
