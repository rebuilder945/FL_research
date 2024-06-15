h=int(input())
N=int(input())
sums=h
for x in range(N):
    sums+=h*(0.5)**(x)
print('%.2f'%sums)    
