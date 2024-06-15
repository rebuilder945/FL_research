h=eval(input())
N=eval(input())
s=h
for i in range(N-1):
    s+=(h/2**i)
print('%.2f'%s)
