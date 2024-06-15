n=eval(input())
x=2
y=1
s=x/y
for i in range(n-1):
    a=x
    x=x+y
    y=a
    s+=x/y
print('%.4f'%(s))






