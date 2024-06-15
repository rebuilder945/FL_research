a=eval(input())
if a<20:
    b=6*a*a+1
elif a<40:
    b=(3*a-60)**0.5
else:
    b=100/(a+1)
print('%.2f'%(b))
