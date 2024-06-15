h=int(input())
n=int(input())
S=h
for x in range(n-1):
    S+=h*(0.5)**(x)
print('%.2f'%(S))



