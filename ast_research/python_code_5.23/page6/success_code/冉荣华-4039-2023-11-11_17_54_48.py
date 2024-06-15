a=float(input)
if a<20:
    print(f'{6*a**2+1:.2f}')
elif 20<=a<=40:
    print(f'{(3*a-60)**(1/2):.2f}')
elif 40<=a:
    print(f'{100/(1+a):.2f}')
