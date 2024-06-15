h=eval(input())
N=eval(input())
Total=0
for i in range(N):
    if i==0:
        Total=h
    else:
        h=h*0.5
        Total=Total+h*2   
print('%.2f'%(Total))
