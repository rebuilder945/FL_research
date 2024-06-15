a=eval(input())
n=eval(input())
if n<=0:
    print(0)
elif n==1:
    print(a)
elif n==2:
    print(2*a)
else:
    N,h=3,2*a
    while N>n:    
       a/=2 
       h+=a
       N+=1
    print('%.2F'%h)
