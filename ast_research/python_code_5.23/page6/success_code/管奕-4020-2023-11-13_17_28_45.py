h=eval(input())
N=eval(input())
H=h
if N==1:
    print('%.2f'%(H))
else:
    for i in range(1,N):
        H=H+2*h*0.1**i
    print('%.2f'%(H))
