
x=2
y=1
a=0
n=int(input())
while n>0:
    a+=x/y
    z=y 
    y=x
    x+=z
    n-=1
print('%.4f'%a)
   
