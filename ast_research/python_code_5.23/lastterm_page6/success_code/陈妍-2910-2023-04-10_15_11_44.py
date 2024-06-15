h=int(input())
N=int(input())
S=h
for x in range(N-1):
    S+=h*(0.5)**x
    print('2f.%'%(S))



