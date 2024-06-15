a=eval(input())
b=eval(input())
c=[]
if b==1:
    print('%.2f'%(a))
else:
    for i in range(1,b):
        d=2*a*0.5**i
        c.append(d)
    print('%.2f'%(a+sum(c)))

