h=eval(input())
n=eval(input())
x=-1
z=0
while n>0:
    n-=1
    x+=1
    z+=2*h*(0.5)**x
    
print(n)
print('%.2f'%(z-10))
