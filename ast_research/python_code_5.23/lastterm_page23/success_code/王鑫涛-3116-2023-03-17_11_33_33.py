a = list(eval(input()))
b = list(eval(input()))
d1 = (a[0]-b[0])**2
d2 = (a[1]-b[1])**2
d = (d1+d2)**(1/2)
print('%.2f'%(d))
