h=int(input())
N=int(input())
p=h
for i in range(N-1):
    p+=h*(0.5)**(i)
print('%.2f'%p)
