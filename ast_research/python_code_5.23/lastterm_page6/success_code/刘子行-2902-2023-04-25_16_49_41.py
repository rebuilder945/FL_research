n=eval(input())
a0=1
a1=2
i=0
s=0
while i<=n-1:
    s=s+a1/a0
    a1=a1+a0
    a0=a1-a0
    i+=1
print('%.4f'%s)
    
