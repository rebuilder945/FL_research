h = eval(input())
N = eval(input())
a = h
for i in range(N-1):
    a += h/(2**i)
print('%.2f'%a)
