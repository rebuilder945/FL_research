h=int(input())
n=int(input())
s=h
if n==1:
    print('%.2f'%s)
else:
    for i in range(n-1):
        h=h*0.5
        s+=2*h
    print('%.2f'%s)

