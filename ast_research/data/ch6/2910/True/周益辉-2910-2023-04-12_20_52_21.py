h=eval(input())
N=eval(input())
s=h
for i in range(N-1):
    h=0.5*h
    s+=h*2
print('%.2f'%(s))
