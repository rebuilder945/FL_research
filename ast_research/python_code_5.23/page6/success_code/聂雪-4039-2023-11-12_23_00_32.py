a=eval(input())
if a<20:
    a=a**2+1
    print('%.2f'%a)
elif a>=20 and a<40:
    a=(3*a-60)**0.5
    print('%.2f'%a)
elif a>=40:
    a=100/(a+1)
    print('%.2f'%a)
