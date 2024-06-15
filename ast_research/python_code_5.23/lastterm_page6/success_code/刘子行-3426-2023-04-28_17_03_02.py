a=eval(input())
def F(x):
    if x<20:
        return 6*x**2+1
    elif x>=20 and x<40:
        return (3*x-60)**(1/2)
    elif x>=40:
        return 100/(x+1)
y=F(a)
print('%.2f'%y)
