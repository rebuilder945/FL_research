a=eval(input())
n=eval(input())
if n<=0:
    print(0)
elif n==1:
    print(a)
elif n==2:
    print(2*a)
else:
    N,h=2,2*a
    while N>=n:
       h=2*a
       N+=1 
       a/=2 
       h+=a
    print('%.2F'%h)
