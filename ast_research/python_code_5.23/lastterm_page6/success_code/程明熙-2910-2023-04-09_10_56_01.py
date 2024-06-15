h=eval(input())
n=eval(input())
s=0
for i in range(0,n):
    s+=2*h*(0.5)**i
s-=10
print('%.2f'%s)
