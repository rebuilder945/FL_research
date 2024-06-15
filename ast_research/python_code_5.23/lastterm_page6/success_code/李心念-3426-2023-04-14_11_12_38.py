x = eval(input())
def f1(n):
    a = 6*n*n+1
    print('%.2f'%a)
def f2(n):
    a = (3*n-60)**(0.5)
    print('%.2f'%a)
def f3(n):
    a = 100/(n+1)
    print('%.2f'%a)
if x < 20:
    f1(x)
elif 20<= x <40:
    f2(x)
else:
    f3(x)
