h=eval(input())
N=eval(input())
sum=h
for i in range(N-1):
    a=h/(2**i)
    sum+=a
print('%.2f'%sum)
