h = int(input())
N = int(input())
s = h
for i in range(1, N):
    s += h * pow(1 / 2, i) *2
s1 =pow(1 / 2, N) * h
print('%.2f'%s1)


