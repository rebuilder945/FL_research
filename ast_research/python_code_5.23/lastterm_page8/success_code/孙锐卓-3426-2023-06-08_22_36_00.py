a=eval(input())
if a<20:
    b=6*a*a+1
if a>=20 and a<40:
    b=(3*a-60)**0.5
if a>=40:
    b=100/(a+1)
print('%.2f'%(b))


