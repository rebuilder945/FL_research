h = int(input())
N = int(input())
s = h
for i in range(1, N):
    s += h * pow(0.5, i) *2
print('%.2f'%s)


