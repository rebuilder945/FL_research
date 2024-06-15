x=eval(input())
if x<20:
    print(f'{6*x*x+1:.2f}')
elif x>=20 and x<40:
    print(f'{(3*x-60)**0.5:.2f}')
else:
    print(f'{100/(x+1):.2f}')
