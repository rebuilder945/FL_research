h=eval(input())
N=int(input())
sum=h
for i in range(N-1):
    sum+=h
    h=h/2
print('%.2f'%(sum))
    
    
