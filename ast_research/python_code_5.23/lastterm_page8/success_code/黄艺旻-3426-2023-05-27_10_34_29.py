a=eval((input()))
if a<20:
    f=6*(a**2)+1
elif a>=40:
    f=100/(a+1)
else:
    f=(3*a-60)**0.5
print('%.2f'%f)
