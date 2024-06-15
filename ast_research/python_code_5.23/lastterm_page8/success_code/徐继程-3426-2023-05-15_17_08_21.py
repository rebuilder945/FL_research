n=eval(input())
if n<20:
    end=6*n**2+1
elif n>=40:
    end=100/(n+1)
else:
    end=(3*n-60)**(1/2)
print('%.2f'%(end))
