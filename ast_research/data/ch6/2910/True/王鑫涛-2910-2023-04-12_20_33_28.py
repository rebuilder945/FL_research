h=eval(input())
n=eval(input())
if n ==1:
    print('%.2f'%h)
else:
    b=h
    for i in range(n-1):
        b+=h
        h/=2
    print('%.2f'%b)
