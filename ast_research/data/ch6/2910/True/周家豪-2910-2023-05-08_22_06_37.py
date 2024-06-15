h=eval(input())
n=eval(input())
total=0
if n==1:
    total=h
    print(f'{total:.2f}')
else:
    total=h
    for i in range(n-1):
        h*=0.5
        total+=2*h
    print(f'{total:.2f}')
