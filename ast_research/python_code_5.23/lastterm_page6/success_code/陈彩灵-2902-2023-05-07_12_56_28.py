n=eval(input())
a=2
b=1
s=0
for i in range(1,n+1):
    s+=a/b
    t=a
    a=a+b
    b=t
print('%.4f'%(s))

