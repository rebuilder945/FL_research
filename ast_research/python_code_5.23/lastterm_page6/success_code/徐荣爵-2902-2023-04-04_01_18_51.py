N = eval(input())
n = 2
m = 1
sums = 0
for i in range(N):
    t = n/m
    sums += t
    n = n + m
    m = n - m
print('%.2f'%sums)
