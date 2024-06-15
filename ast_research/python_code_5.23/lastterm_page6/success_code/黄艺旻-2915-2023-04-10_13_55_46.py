N=eval('')
M=eval(input())
a=N%10
b=((N-a)%100)/10
c=(N-a-b)/100
N=a**3+b**3+c**3
if M>=N:
    print(N)
else:
    print('none')
