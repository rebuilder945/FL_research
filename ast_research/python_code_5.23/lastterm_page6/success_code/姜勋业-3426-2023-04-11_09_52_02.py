x=eval(input())
if x<20:
    k=x**2*6+1
elif x>=20 and x<40:
    k=(3*x-60)**(1/2)
elif x>=40:
    k=100/(x+1)
print('%.2f'%k)
