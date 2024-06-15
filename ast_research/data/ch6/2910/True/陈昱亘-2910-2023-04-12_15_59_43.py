h=eval(input())
N=eval(input())
i=1
s=h
while i<N:
    s+=h
    h=h*0.5
    i+=1
print('%.2f'%(s))
