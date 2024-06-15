H=eval(input())
N=eval(input())
x=H
for i in range(N-2):
    x+=H*(1/2)**(i+1)
x+=H
print('%.2f'%(x))


