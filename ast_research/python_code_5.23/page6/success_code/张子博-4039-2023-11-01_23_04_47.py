x=eval(input())
m=0
if x<20:
    m=6*(x**2)+1
elif x<40:
    m=(3*x-60)**0.5
else:
    m=100/(x+1)
print('%.2f'%m)
    
