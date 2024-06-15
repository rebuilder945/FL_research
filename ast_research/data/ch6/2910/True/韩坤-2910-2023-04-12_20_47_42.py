h=eval(input())
n=eval(input())
if n==1:
    x=h
else:
    x=h
    for i in range(n-1):
        x=x+h/(2**i)
print('%.2f'%x)
