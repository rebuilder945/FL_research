h=eval(input())
N=eval(input())
s=10
for i in range(N-1):
    h=0.5*h
    s+=h*2
print('%.2f'%(s))
