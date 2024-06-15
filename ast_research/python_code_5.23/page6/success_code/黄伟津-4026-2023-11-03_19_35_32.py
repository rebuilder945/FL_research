n = eval(input())
fSum = 0
fz = 2
fm = 1
for i in range(n):
    fSum += fz / fm
    fz,fm = fm,fz
    fz += fm
print(f'{fSum:.4f}')
