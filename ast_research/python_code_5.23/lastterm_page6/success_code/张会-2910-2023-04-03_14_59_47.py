h = eval(input())
N = eval(input())
a = 0
b = 0
if N <= 2:
    b += N*h
else:
    for i in range(1,N-1):
        a += h/(2**i)
        b = 20 +a
print('%.2f'%b)
