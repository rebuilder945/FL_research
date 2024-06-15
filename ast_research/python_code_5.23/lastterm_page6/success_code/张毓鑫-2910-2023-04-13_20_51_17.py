a=eval(input())
b=eval(input())
c=-a
for i in range(b):
    c+=2*a
    a*=.5
print('%.2f'%c)
