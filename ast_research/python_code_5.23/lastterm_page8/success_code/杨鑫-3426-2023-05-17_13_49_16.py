def f(x):
    if x < 20:
        y = 6*x*x+1
    elif 20 <= x < 40:
        y = (3*x-60)**0.5
    elif x >= 40:
        y = 100/(x+1)
    return '%.2f'%y
x = float(input())
print(f(x)) 
