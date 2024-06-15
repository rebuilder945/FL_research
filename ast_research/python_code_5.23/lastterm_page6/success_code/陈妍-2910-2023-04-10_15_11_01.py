h=int(input())
N=int(input())
for x in range(N-1):
    h+=h*(0.5)**x
    print('2f.%'%(h))



