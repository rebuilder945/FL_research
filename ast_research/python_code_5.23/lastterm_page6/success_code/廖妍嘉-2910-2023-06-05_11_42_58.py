h=eval(input())
N=eval(input())
if N==1:
    print('%.2f'%(h))
else:
    h1=h
    for i in range(1,N):
        h1=h1*0.5
        h=h+h1*2
        i+=1
    print('%.2f'%(h))

        

