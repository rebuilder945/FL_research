h=eval(input())
N=eval(input())
if N==1:
    print('%.2f'%(h))
else:
    for i in range(1,N):
        h1=h*(0.5**(i))
        h=h+h1*2
        i+=1
    print('%.2f'%(h))

        

